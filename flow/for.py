#!/usr/bin/python
# Filename: for.py

for i in range(1, 5):
    if i == 3:
        break
    else:
        print i
else:
    print 'The for loop is over'