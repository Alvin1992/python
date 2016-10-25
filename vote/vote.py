#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
from threading import Thread
from time import time
import cPickle


class Vote(Thread):
    def __init__(self, proxy):
        Thread.__init__(self)
        self.proxy = proxy
        self.url = 'http://www.ccrpf.org.cn/Vote/VoteSave?VoteClass_ID=b3ec4f87-0344-4255-abd0-2c42c892b048&Vote_ID=1ff527f0-3b6e-4f98-894a-39ca3becd43e'
        self.header = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, sdch",
            "Accept-Language": "zh-CN,zh;q=0.8",
            "Cache-Control": "no-cache",
            "Host": "www.ccrpf.org.cn",
            "Referer": "http://www.ccrpf.org.cn/Vote/Index/b3ec4f87-0344-4255-abd0-2c42c892b048",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36"
        }
        self.timeout = 20

    def run(self):
        proxy_handle = urllib2.ProxyHandler({"http": r'http://%s' % self.proxy})
        opener = urllib2.build_opener(proxy_handle)
        urllib2.install_opener(opener)
        try:
            req = urllib2.Request(self.url, headers=self.header)
            res = urllib2.urlopen(req, timeout=self.timeout)
            result = res.read().decode('utf-8')
            print result
            pos = result.find('true')
            if pos != 1:
                addnum()
            else:
                pass
        except Exception, e:
            print e.message, 'error'


def addnum():
    global n
    n += 1


def shownum():
    return n


n = 0

threads = []

f = file('proxy.txt')

proxylist = cPickle.load(f)

for proxy in proxylist:
    t = Vote(proxy)
    threads.append(t)

if __name__ == '__main__':
    start_time = time()
    for i in threads:
        i.start()
    for i in threads:
        i.join()
    print '%s votes have been voted successfully using %s seconds' % (shownum(), time() - start_time)
