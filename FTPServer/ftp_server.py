#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import socket
from datetime import datetime

import conf


class SimpleServer(object):
    """
    FTP server
    """

    def user_auth(self, data_list, conn):
        with open(conf.db_path, "r", encoding='utf-8') as f:
            for line in f:
                if line.strip() == '|'.join(data_list):
                    return True
        return False

    def create_home(self, user_home):
        dir_path = os.path.join(conf.ftp_path, user_home)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        os.chdir(dir_path)

    def save_file(self, file_name, file_data):
        data_list = file_data.split("\n")
        with open(file_name, 'w') as f:
            for line in data_list:
                f.write(line)
                f.write('\n')

    def send_file(self, file_name, conn):
        try:
            with open(file_name, 'rb') as f:
                conn.send(f.read())
        except FileNotFoundError:
            conn.send(bytes(conf.FAIL_CODE, encoding="utf-8"))

    def show_file_list(self, conn):
        cwd = os.getcwd()
        res = os.listdir(cwd)
        conn.send(bytes(str(res), encoding="utf-8"))


def main():
    sever = socket.socket()
    sever.bind((conf.ip, conf.port))
    sever.listen()
    sever_obj = SimpleServer()
    while True:
        conn, addr = sever.accept()
        username = None
        while True:
            try:
                data = str(conn.recv(conf.size))
            except ConnectionResetError:
                if username:
                    print("{} {} 异常退出！".format(datetime.now(), username))
                else:
                    print("{} {} 断开连接！".format(datetime.now(), addr[0]))
                break
            data_list = data[2:-1].split('|')
            if data_list[0] == "login":
                res = sever_obj.user_auth(data_list[1:], conn)
                if res:
                    sever_obj.create_home(data_list[1])
                    username = data_list[1]
                    print("{} {} 登陆！".format(datetime.now(), username))
                    conn.send(bytes(conf.SUCCESS_CODE, encoding='utf-8'))
                else:
                    conn.send(bytes(conf.FAIL_CODE, encoding='utf-8'))
            elif data_list[0] == "upload":
                sever_obj.save_file(data_list[1], data_list[2])
            elif data_list[0] == "download":
                sever_obj.send_file(data_list[1], conn)
            elif data_list[0] == "ls":
                sever_obj.show_file_list(conn)
            elif data_list[0] == "quit":
                print("{} {} 退出！".format(datetime.now(), username))
                break


if __name__ == '__main__':
    main()
