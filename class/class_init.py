#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Filename: class_init.py

class Person:
    def __init__(self, name):
        self.name = name

    def sayHi(self):
        print 'Hello, my name is', self.name

p = Person('Alvin')
p.sayHi()
