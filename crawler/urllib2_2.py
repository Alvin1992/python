#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Filename: urllib2_2.py

# request对象映射HTTP请求
# 通过调用urlopen并传入request对象，返回一个相关请求的response对象
# 可以在response中调用.read()

import urllib2
req = urllib2.Request('http://www.baidu.com')
response = urllib2.urlopen(req)
the_page = response.read()
print the_page
