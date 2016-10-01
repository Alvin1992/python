#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Filename: addressBook.py

import time, cPickle, sys, os

# 版本信息
info = {}
# 联系人保存的表
addressBook = {'name': '13100000001', 'kate': '13000000001'}
# 保存的文件路径
dataPath = '/d/fanrx/addressBook.data'


def updateTime():
    """Update modify time"""
    info['lastModify'] = time.strftime('%Y-%m-%d %H:%M:%S')


def addContact(book, name, addr):
    """Add a contact to addressBook"""
    book[name] = addr

if __name__ == '__main__':
    args = sys.argv
    length = len(args)

    # 没有额外的参数传递时打印所有的联系人
    if length < 2:
        for item in addressBook:
            print item, addressBook[item]
        sys.exit()

    firstArg = args[1]
    # 没有短命令或者长命令的情况
    if length == 2:
        result = addressBook[firstArg]
        if result:
            print 'The address of %s is' % (firstArg, result)
        else:
            print 'No contact information of %s' % firstArg

    # 第一个参数如果以-开始，表示进行的是增删改查
    # if firstArg.startswith('-'):
    #     if firstArg[1:] == 'a':
    #         addContact(addressBook, args[2], args[3])
    #     sys.exit()
