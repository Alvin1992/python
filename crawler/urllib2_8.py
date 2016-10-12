#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Filename: urllib2_8.py

# urlopen返回的应答对象response(或者HTTPError实例)有两个很有用的方法info()和geturl()
# geturl()返回获取的真实的URL，这个很有用，因为urlopen(或者opener对象使用的)或许会有重定向。

import urllib2

# old_url = 'http://rrurl.cn/b1UZuP'
#
# response = urllib2.urlopen(old_url)
#
# print 'Old url:', old_url
# print 'New url:', response.geturl()

# info()
# 返回对象的字典对象，该字典描述了获取的页面情况。通常是服务器发送的特定头headers。
# 目前是httplib.HTTPMessage 实例。

res = urllib2.urlopen('http://www.baidu.com')
print 'Info:'
print res.info()
