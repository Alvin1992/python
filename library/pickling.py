#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Filename: pickling.py

import cPickle as p

# 保存对象的文件名
shoplistfile = 'shoplist.data'

# 要保存的对象
shoplist = ['apple', 'mango', 'orange']

# 写入到对象
f = file(shoplistfile, 'w')

# 复制对象到文件
p.dump(shoplist, f)
f.close()

# 删除对象
del shoplist

# 从保存的文件中读取
f = file(shoplistfile)
storedlist = p.load(f)
print storedlist
