#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Filename: create-file1.py

import os
import time

# 写入路径
dirPath = '/home/alvin/projects/'
today = dirPath + time.strftime('%Y-%m-%d')

if not os.path.exists(today):
    os.mkdir(today)

filePath = today + os.sep + time.strftime('%H%M%S') + '.txt'
f = file(filePath, 'w')
f.write('time now is ' + time.strftime('%Y-%m-%d %H:%M:%S'))
f.close()
