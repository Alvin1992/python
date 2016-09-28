#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Filename: backup_ver2.py

import os
import time
import sys

version = 1.0
about = 'This is a script for backup, established in 2016-09-28'


def backup():
    # 要备份的文件或者文件夹列表
    source = ['/e/fanrx/bar', '/e/fanrx/foo']

    # 保存备份的路径
    target_dir = '/d/back_alvin/'

    # 以当前日期作为下级目录
    today = target_dir + time.strftime('%Y%m%d')

    # 以当前时间作为压缩文件名
    now = time.strftime('%H%M%S')

    # 备份注释
    comment = raw_input('此次备份的说明 --> ')
    if len(comment) == 0:
        target = today + os.sep + now + '.zip'
    else:
        target = today + os.sep + now + '_' + comment.replace(' ', '_') + '.zip'

    # 创建下级目录
    if not os.path.exists(today):
        os.mkdir(today)
        print 'Successfully created directory', today

    # 执行压缩的命令
    zip_command = "zip -qr '%s' %s" % (target, ' '.join(source))

    # 执行压缩
    if os.system(zip_command) == 0:
        print 'backup success'
    else:
        print 'backup failed'

if __name__ == '__main__':
    if len(sys.argv) > 1:
        params = sys.argv[1:]
        for param in params:
            if param == '-v':
                print version
            elif param == '-a':
                print about
    else:
        backup()
else:
    pass
