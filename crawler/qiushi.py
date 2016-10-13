#!/usr/bin/python
# -*- coding: utf-8 -*-

from pyquery import PyQuery as pq
import urllib2
import sys

req = urllib2.Request('http://www.qiushibaike.com/hot/page/2/')
req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64)')
response = urllib2.urlopen(req)
d = pq(response.read())

allBlocks = d('.article')
for block in allBlocks:
    content = d(block).find('.content span').html()
    comment = d(block).find('.main-text').html()
    print ('\n' + content.replace('<br />', '\n') + '\n')
    if not comment:
        print '没有神评论'
    else:
        print '神评论 %s' % comment
    cmd = str(raw_input('next?'))
    if cmd == 'quit':
        sys.exit()
