#!/usr/bin/env python
# -*- coding:utf-8 -*-


import conf

user_list = ['Lucy|123', 'Tom|123456']


def main():
    with open(conf.db_path, 'w') as f:
        for i in user_list:
            f.write(i)
            f.write('\n')


if __name__ == '__main__':
    main()
