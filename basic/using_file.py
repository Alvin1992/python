#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Filename: using_file.py

poem = '''\
Programming is fun
When the work is done
if you wanna make your work also fun:
        use Python!
'''

f = file('poem.txt', 'w')
f.write(poem)
f.close()

f = file('poem.txt') #默认是读模式
while True:
    line = f.readline()
    if len(line) == 0: # 0表示EOF
        break
    print line,
f.close()
