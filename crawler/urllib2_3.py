#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Filename: urllib2_3.py

# 一般的HTML表单，data需要编码成标准形式，然后作为data参数传到Request对象
# 编码工作使用urllib的函数

import urllib
import urllib2

url = 'https://ssl.mail.163.com/regall/unireg/call.do;jsessionid=8DD1A33F74474CF0319A81A0AB928F2F?cmd=register.start'

values = {
    'flow': 'mobile',
    'mobile': '13108888888',
    'uid': '13100888888@163.com',
    'acode': '123456',
    'mark': 'mobile_start',
    'password': '123456789sdf',
    'confirmPassword': '123456789sdf',
    'uapw': 'true',
    'from': '126mail'
}

data = urllib.urlencode(values)  # 编码
req = urllib2.Request(url, data)  # 发送请求时传data表单
response = urllib2.urlopen(req)  # 接受反馈的信息
the_page = response.read()  # 读取反馈的信息
print the_page
