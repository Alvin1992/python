#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Filename: str_methods.py

name = 'Alvin'

if name.startswith('Al'):
    print 'Yes, the string starts with "Al"'

if 'a' in name:
    print 'Yes, it contains the string "a"'

if name.find('in') != -1:
    print 'Yes, it contains the string "in"'

delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'India', 'China']

print delimiter.join(mylist)