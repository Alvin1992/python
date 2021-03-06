#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Filename: addressBook.py

import time
import cPickle
import sys
import os

# 联系人保存的表
addressBook = {}
# 保存的文件路径
dataPath = '/d/fanrx/addressBook.data'


def updateTime(book):
    """Update modify time"""
    book['lastModify'] = time.strftime('%Y-%m-%d %H:%M:%S')


def addContact(book, name, addr):
    """Add a contact to addressBook"""
    try:
        result = book[name]
        book[name] = addr
        print 'Change contact information of %s successfully from %s to %s' % (name, result, addr)
    except KeyError:
        book[name] = addr
        print 'Add contact information of %s successfully' % name


def findContact(book, name):
    try:
        result = book[name]
        print 'The address of %s is %s' % (name, result)
        sys.exit()
    except KeyError:
        print 'No contact information of %s' % name
        sys.exit()


def delContact(book, name):
    try:
        del book[name]
        print 'Delete contact of %s successfully' % name
    except KeyError:
        print 'No contact information of %s' % name


if __name__ == '__main__':
    if os.path.exists(dataPath):
        fileObject = file(dataPath)
        addressBook = cPickle.load(fileObject)
    args = sys.argv
    length = len(args)

    # 没有额外的参数传递时打印所有的联系人
    if length < 2:
        if len(addressBook) == 0:
            print 'No contact'
        else:
            for item in addressBook:
                if item != 'lastModify':
                    print item, addressBook[item]
        sys.exit()

    firstArg = args[1]
    # 第一个参数如果以-开始，表示进行的是增删改查
    if firstArg.startswith('-'):
        option = firstArg[1:]
        if option == 's':
            findContact(addressBook, args[2])
        elif option == 'a' or option == 'c':
            addContact(addressBook, args[2], args[3])
            updateTime(addressBook)
        elif option == 'd':
            delContact(addressBook, args[2])
            updateTime(addressBook)
        elif option == 'm':
            try:
                print 'Last change of addressBook is %s' % addressBook['lastModify']
            except KeyError:
                print 'This is your first operation'
            sys.exit()
        elif option == 'n':
            print 'Total number of addressBook is %d' % (len(addressBook)-1)
            sys.exit()
            # 没有短命令或者长命令的情况
    elif length == 2:
            findContact(addressBook, firstArg)
    elif length == 3:
            addContact(addressBook, args[1], args[2])

    f = file(dataPath, 'w')
    cPickle.dump(addressBook, f)
    f.close()
