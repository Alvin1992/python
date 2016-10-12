#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Filename: urllib2_7.py

# 为HTTPError和URLError做准备
# 两种方法，第一种如下

# import urllib2
#
# req = urllib2.Request('http://bbs.csdn.net/callmewhy')
# try:
#     urllib2.urlopen(req)
# except urllib2.HTTPError, e:
#     print 'The sever could\'nt fulfill the request.'
#     print 'Error code:', e.code
# except urllib2.URLError, e:
#     print 'We failed to reach a server.'
#     print 'Reason:', e.reason
# else:
#     print 'No exception was raised.'
# except HTTPError 必须在第一个，否则except URLError将同样接受到HTTPError 。
# 因为HTTPError是URLError的子类，如果URLError在前面它会捕捉到所有的URLError（包括HTTPError ）。

# 第二种
import urllib2

req = urllib2.Request('http://bbs.csdn.net/callmewhy')
try:
    urllib2.urlopen(req)
except urllib2.URLError, e:
    if hasattr(e, 'code'):
        print 'The sever could\'nt fulfill the request.'
        print 'Error code:', e.code
    elif hasattr(e, 'reason'):
        print 'We failed to reach a server.'
        print 'Reason:', e.reason
else:
    print 'No exception was raised.'
