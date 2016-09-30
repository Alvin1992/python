#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Filename: backup_ver7.py

import os
import time
import sys
import tarfile


def backup(otherList):

    # 要备份的文件或者文件夹列表
    source = ['/d/fanrx/bar', '/d/fanrx/foo']

    # 额外的文件夹或者文件
    if len(otherList) > 0:
        source.extend(otherList)

    # 保存备份的路径
    target_dir = '/d/back_alvin/'

    # 以当前日期作为下级目录
    today = target_dir + time.strftime('%Y%m%d')

    # 以当前时间作为压缩文件名
    now = time.strftime('%H%M%S')

    # 备份说明
    comment = raw_input('此次备份的说明 --> ')
    if len(comment) == 0:
        target = today + os.sep + now + '.tar.gz'
    else:
        target = today + os.sep + now + '_' + comment.replace(' ', '_') + '.tar.gz'

    # 创建下级目录
    if not os.path.exists(today):
        os.mkdir(today)
        print 'Successfully created directory', today

    # 创建压缩包名
    tar = tarfile.open(target, 'w:gz')

    # 创建压缩包
    for filePath in source:
        for root, dirs, files in os.walk(filePath):
            if len(files) == 0 and len(dirs) == 0:
                tar.add(root)
            for f in files:
                fullpath = os.path.join(root, f)
                tar.add(fullpath)
    tar.close()
info = {
    "version": 1.0,
    "about": 'This is a script for backup, established in 2016-09-28'
}
fileList = []
if __name__ == '__main__':
    params = sys.argv[1:]
    if len(params) > 0:
        if '-v' in params:
            print info['version']
        elif '-a' in params:
            print info['about']
        else:
            for pathItem in params:
                if os.path.exists(pathItem):
                    fileList.append(pathItem)
            backup(fileList)
    else:
        backup(fileList)
