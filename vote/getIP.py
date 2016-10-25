#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
from random import choice
import requests
import bs4
import cPickle

url = "http://www.xicidaili.com/nn/1"
headers = { "Accept": "text/html,application/xhtml+xml,application/xml;",
            "Accept-Encoding": "gzip",
            "Accept-Language": "zh-CN,zh;q=0.8",
            "Referer": "http://www.xicidaili.com/",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36"
}
r = requests.get(url, headers=headers)
soup = bs4.BeautifulSoup(r.text, 'html.parser')
data = soup.table.find_all("td", limit=1000)
ip_compile = re.compile(r'<td>(\d+\.\d+\.\d+\.\d+)</td>')
port_compile = re.compile(r'<td>(\d+)</td>')
ip = re.findall(ip_compile, str(data))
port = re.findall(port_compile, str(data))
ips = [":".join(i) for i in zip(ip, port)]
print u'获取的IP总数：{ip_len}'.format(ip_len=len(ips))
print u"代理IP列表：{ip_list}".format(ip_list=ips)
print u"随机在代理IP列表中选一个IP：{ip}".format(ip=choice(ips))
f = file('proxy.txt', 'w')
cPickle.dump(ips, f)
f.close()
