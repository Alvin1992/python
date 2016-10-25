#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
from threading import Thread
from time import time


class Vote(Thread):
    def __init__(self, proxy):
        Thread.__init__(self)
        self.proxy = proxy
        self.url = 'http://www.ccrpf.org.cn/Vote/Index'
        self.timeout = 10

    def run(self):
        proxy_handle = urllib2.ProxyHandler({"http": r'http://%s' % self.proxy})
        opener = urllib2.build_opener(proxy_handle)
        urllib2.install_opener(opener)
        try:
            req = urllib2.urlopen(self.url, timeout=self.timeout)
            result = req.read().decode('gbk')
            print result
            return
            pos = result.find(u'成功')
            if pos > 1:
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

proxylist = open('proxy.txt', 'r')

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