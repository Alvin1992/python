#!/usr/bin/python
# -*- coding: utf-8 -*-

from pyquery import PyQuery as pq
import urllib2
import sys

req = urllib2.Request('http://www.qiushibaike.com/hot/page/2/')
req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64)')
response = urllib2.urlopen(req)
d = pq(response.read().decode('utf-8'))

allBlocks = d('.article')
for block in allBlocks:
    block = d(block)
    content = block.find('.content span').html()
    author = block.find('.author h2').html()
    comment = block.find('.main-text').html()
    upvote = block.find('.stats-vote i').html()
    commentNum = block.find('.stats-comments i').html()
    print u'\n-----------作者：%s 好评：%s 评论数：%s-------------' % (author, upvote, commentNum)
    try:
        print ('\n' + content.replace('<br />', '\n') + '\n')
    except UnicodeEncodeError, e:
        print u'编码错误'
    print u'-----------------------------------------------------------------'
    if not comment:
        print u'\n没有神评论'
    else:
        print u'\n神评论 %s' % comment
    cmd = str(raw_input(u'\nquit or enter \n'))
    if cmd == 'quit':
        sys.exit()
