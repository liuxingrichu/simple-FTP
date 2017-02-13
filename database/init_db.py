#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os

import conf


user_list = ['Lucy|123', 'Tom|123456']


def main():
    if not os.path.exists(conf.db_path):
        os.makedirs(conf.db_path)
    with open(conf.file_path, 'w+') as f:
        for i in user_list:
            f.write(i)
            f.write('\n')


if __name__ == '__main__':
    main()
