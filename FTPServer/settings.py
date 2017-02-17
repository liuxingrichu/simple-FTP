#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os

ftp_path = r"d:\FTP_test"
db_path = os.path.join(ftp_path, "etc")
file_path = os.path.join(db_path, "user_info.db")
SUCCESS_CODE = '200'
FAIL_CODE = '404'
size = 1024
ip = 'localhost'
port = 6969