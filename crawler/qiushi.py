#!/usr/bin/python
# -*- coding: utf-8 -*-

# pip安装cssselector,lxml,pyquery
# 安装lxml需要vs c++ for python和lxml.whl文件
from pyquery import PyQuery as pq
import urllib2

req = urllib2.Request('http://www.qiushibaike.com/hot/page/3/')
req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64)')
response = urllib2.urlopen(req)
d = pq(response.read())

foot = d('.content span')

for item in foot:
    print (d(item).html().replace('<br />', '\n') + '\n\n')
