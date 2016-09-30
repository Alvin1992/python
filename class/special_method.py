#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Filename: special_method.py


class Foo:
    """A test class"""
    def __str__(self):
        return '这是一个测试的类'

    def __len__(self):
        return 2

bar = Foo()
print bar

print len(bar)
