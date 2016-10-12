#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Filename: urllib2_5.py

# HTTPError是urlError的子类，通常在特定HTTP URLs中产生。
# 通常，URLError在没有网络连接(没有路由到特定服务器)，或者服务器不存在的情况下产生。
# 这种情况下，异常同样会带有"reason"属性，它是一个tuple
# 包含了一个错误号和一个错误信息

import urllib2

req = urllib2.Request('http://www.baidu.com')

try:
    urllib2.urlopen(req)
except urllib2.URLError, e:
    print e.reason
