#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Filename: reference.py

print 'a simple task'
fruit = ['apple', 'orange', 'mango', 'banana']
yourFruit = fruit

del fruit[0]

print 'fruit is', fruit
print 'your fruit is', yourFruit

print 'copy by making a full slicing'

yourFruit = fruit[:]
del fruit[0]

print 'fruit is', fruit
print 'your fruit is', yourFruit