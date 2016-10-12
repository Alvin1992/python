#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Filename: urllib2_6.py

# HTTPError
# 因为默认的处理器处理了重定向(300以外号码)，并且100-299范围的号码指示成功，所以你只能看到400-599的错误号码。
# BaseHTTPServer.BaseHTTPRequestHandler.response是一个很有用的应答号码字典，显示了HTTP协议使用的所有的应答号。

import urllib2

req = urllib2.Request('http://blog.csdn.net/callmewhy')

try:
    urllib2.urlopen(req)
except urllib2.HTTPError, e:
    print e.code
