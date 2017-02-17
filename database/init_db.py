#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
<<<<<<< HEAD
import sys
=======
>>>>>>> 3af09226973d2825a3fdedf3bddc2269089a7728

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_PATH)

from FTPServer import settings


user_list = ['Lucy|123', 'Tom|123456']


def main():
<<<<<<< HEAD
    if not os.path.exists(settings.db_path):
        os.makedirs(settings.db_path)
    with open(settings.file_path, 'w+') as f:
=======
    if not os.path.exists(conf.db_path):
        os.makedirs(conf.db_path)
    with open(conf.file_path, 'w+') as f:
>>>>>>> 3af09226973d2825a3fdedf3bddc2269089a7728
        for i in user_list:
            f.write(i)
            f.write('\n')


if __name__ == '__main__':
    main()
