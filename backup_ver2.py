#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Filename: backup_ver2.py

import os
import time

# 要备份的文件或者文件夹列表
source = ['/e/fanrx/bar', '/e/fanrx/foo']

# 保存备份的路径
target_dir = '/d/back_alvin/'

# 以当前日期作为下级目录
today = target_dir + time.strftime('%Y%m%d')

# 以当前时间作为压缩文件名
now = time.strftime('%H%M%S')

# 创建下级目录
if not os.path.exists(today):
    os.mkdir(today)
    print 'Successfully created directory', today

# 备份文件的路径及名字
target = today + os.sep + now + '.zip'

# 执行压缩的命令
zip_command = "zip -qr '%s' %s" % (target, ' '.join(source))

# 执行压缩
if os.system(zip_command) == 0:
    print 'backup success'
else:
    print 'backup failed'