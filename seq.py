#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Filename: seq.py

fruit = ['mango', 'apple', 'banana', 'orange']

# indexing operation
print 'Item 0 is', fruit[0]
print 'Item 1 is', fruit[1]
print 'Item -1 is', fruit[-1]
print 'Item -2 is', fruit[-2]

# slicing operation
print 'Item 1 to 3 is', fruit[1:3]
print 'Item 2 to end is', fruit[2:]
print 'Item 1 to -1 is', fruit[1:-1]
print 'Item from start to end', fruit[:]

# slicing on a string
name = 'Alvin'
print 'Character 1 to 3 is', name[1:3]
print 'Character 2 to end is', name[2:]
print 'Character 1 to -1 is', name[1:-1]
print 'Character from start to end', name[:]