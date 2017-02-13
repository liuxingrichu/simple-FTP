#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import re
import socket
import sys

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_PATH)

import settings

templates = ["【1】登录", "【2】上传文件", "【3】下载文件", "【4】查看文件列表", \
             "【5】退出"]


class SimpleClient(object):
    """
    FTP client
    """

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self, conn):
        user_info = "|".join(["login", self.username, self.password])
        conn.send(bytes(user_info, encoding='utf-8'))
        return conn.recv(settings.size)

    def upload(self, file_name, client):
        data_list = ['upload', file_name]
        try:
            with open(file_name, 'r') as f:
                data_list.append(f.read())
        except FileNotFoundError:
            print("\t\033[0;31m文件不存在\033[1m")
            return False
        client.send(bytes("|".join(data_list), encoding='utf-8'))
        return True

    def download(self, file_name, client):
        data_list = ['download', file_name]
        client.send(bytes("|".join(data_list), encoding='utf-8'))
        file_data = client.recv(settings.size)
        if file_data == bytes(settings.FAIL_CODE, encoding='utf-8'):
            return settings.FAIL_CODE
        with open(file_name, 'wb') as f:
            f.write(file_data)
        return settings.SUCCESS_CODE

    def show_file_list(self, data):
        start_index = data.index('[') + 1
        tmp = re.split("[',]", data[start_index:-2])
        data_list = []
        for i in tmp:
            if i.strip():
                data_list.append(i)
        print("文件列表".center(30, '-'))
        for i in data_list:
            print(i)
        print("end".center(33, '-'))

    def logout(self, conn):
        conn.close()


def main():
    client = socket.socket()
    client.connect((settings.ip, settings.port))
    user_status = False

    while True:
        print("FTP客户端".center(67, "-"))
        print("{} {} {} {} {}".format(templates[0], templates[1], templates[2],
                                      templates[3], templates[4]))
        print("end".center(70, '-'))

        choice = input(">>").strip()
        if choice == "1":
            if not user_status:
                username = input("Enter username : ").strip()
                password = input("Enter password :").strip()
                client_obj = SimpleClient(username, password)
                res = client_obj.login(client)
                if res == bytes(settings.SUCCESS_CODE, encoding='utf-8'):
                    print("\t\033[0;32m欢迎%s登陆\033[1m" % username)
                    user_status = True
                else:
                    print("\t\033[0;31m用户名或密码错误！\033[1m")
            else:
                print("\t\033[0;31m用户已登陆！\033[1m")
        elif choice == "2":
            if user_status:
                print("\t请输入上传文件名称，例如test.txt")
                file_name = input("Enter upload file name : ").strip()
                res = client_obj.upload(file_name, client)
                if res:
                    print("\t\033[0;32m文件上传成功！\033[1m")
            else:
                print("\t\033[0;31m请登录\033[1m")
        elif choice == "3":
            if user_status:
                print("\t请输入下载文件名称，例如test.txt")
                file_name = input("Enter download file name : ").strip()
                res = client_obj.download(file_name, client)
                if res == settings.SUCCESS_CODE:
                    print("\t\033[0;32m文件下载成功！\033[1m")
                else:
                    print("\t\033[0;31m文件不存在！\033[1m")
            else:
                print("\t\033[0;31m请登录！\033[1m")
        elif choice == "4":
            if user_status:
                client.send(bytes('ls', encoding='utf-8'))
                data = client.recv(settings.size)
                client_obj.show_file_list(str(data))
            else:
                print("\t\033[0;31m请登录！\033[1m")
        elif choice == "5":
            if user_status:
                client.send(bytes("quit", encoding='utf-8'))
                client_obj.logout(client)
                break
            else:
                print("\t\033[0;31m请登录！\033[1m")
        else:
            print("\t\033[0;31m请输入正确选项！\033[1m")
            continue


if __name__ == '__main__':
    main()
