#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import sys


BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_PATH)

from FTPServer import settings


user_list = ['Lucy|123', 'Tom|123456']


def main():
    if not os.path.exists(settings.db_path):
        os.makedirs(settings.db_path)
    with open(settings.file_path, 'w+') as f:
        for i in user_list:
            f.write(i)
            f.write('\n')


if __name__ == '__main__':
    main()
