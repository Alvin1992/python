#!/usr/bin/python
# -*- coding: utf-8 -*-
# Filename: tieba_simple.py

# 在windows下打印包含中文的字符串要用.decode('utf-8').encode('gbk')处理后才不会乱码
# linux下不需要这样处理

import urllib2
import string


def tiezi(url, startPage, endPage):
    """Get specified page's content of tiezi"""
    for i in range(startPage, endPage+1):
        filename = string.zfill(i, 5) + '.html'  # use six-digit filename
        print '正在下载第' + str(i) + '个网页，并存储为' + filename + '......'
        f = file(filename, 'w+')
        content = urllib2.urlopen(url + str(i)).read()
        f.write(content)
        f.close()


# input parameters
bdurl = str(raw_input('请输入贴吧的地址，去掉pn=后面的数字：\n'))
startPage = int(raw_input('请输入开始的页数：\n'))
endPage = int(raw_input('请输入终点的页数：\n'))

tiezi(bdurl, startPage, endPage)
