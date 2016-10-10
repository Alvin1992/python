#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Filename: urllib2_4.py

# 如果没有传递参数，默认使用GET方式
# data同样也可以在GET请求的url本身上面编码传送

# import urllib
# import urllib2
#
# data = {}
#
# data['id'] = '13'
# data['code'] = '1878607694'
#
# url_values = urllib.urlencode(data)
# print url_values
#
# url = 'http://192.168.1.88:2000/store'
# full_url = url + '?' + url_values
#
# response = urllib2.urlopen(full_url)
# page = response.read()
# print page

# 设置headers，有些网站不喜欢被程序访问，urllib2默认将自己作为'user-agent': 'Python-urllib/2.7'
# 浏览器确认自己身份是通过User-Agent头
# 两种方法一是将headers作为Request的第三个参数
# 二是使用add_header方法

import urllib
import urllib2

data = {}

data['id'] = '13'
data['code'] = '1878607694'

url_values = urllib.urlencode(data)
print url_values

url = 'http://192.168.1.88:2000/store'
full_url = url + '?' + url_values

req = urllib2.Request(full_url)
req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64)')
response = urllib2.urlopen(req)
page = response.read()
print page
