#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Filename: three-digit.py
# 1,2,3,4能组成的不重复且不相等的三位数一共有多少，分别是哪些
result = []

for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if (i != j) and (i != k) and (j != k):
                result.append(i*100+j*10+k)
print '一共有%d个三位数' % len(result)
print '分别是',
for num in result:
    print num,
