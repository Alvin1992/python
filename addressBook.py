#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Filename: addressBook.py

import time, cPickle, sys, os

# 版本信息
info = {}
# 联系人保存的表
addressBook = {}
# 保存的文件路径
dataPath = '/d/fanrx/addressBook.data'


def updateTime():
    """Update modify time"""
    info['lastModify'] = time.strftime('%Y-%m-%d %H:%M:%S')


def addContact(book, name, addr):
    """Add a contact to addressBook"""
    book[name] = addr

if __name__ == '__main__':
    print os.path.split(dataPath)
