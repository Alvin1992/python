#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Filename: backup_ver1.py

import os
import time

# 要备份的文件列表
source = ['/e/fanrx/foo', '/e/fanrx/bar']
# windows下使用source = [r'C:\Documents', r'D:\Work']这样的格式
# 或者'C:\\Documents'

# 保存备份的目录
target_dir = '/d/back_alvin/'

# 以zip格式保存
# 压缩文件的名字是当前的日期和时间
target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'

# linux或者Unix下使用zip的命令将文件压缩
zip_command = "zip -qr '%s' %s" % (target, ' '.join(source))

# 执行备份
if os.system(zip_command) == 0:
    print 'Successful back to', target
else:
    print 'Backup Failed'
