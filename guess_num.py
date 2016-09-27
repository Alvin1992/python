#!/usr/bin/python
# Filename: guess_num.py

import random

count = 0
randNum = int(random.random()*100 + 1)

while True:
    guess = int(raw_input('Enter integer: '))
    count += 1
    if guess == randNum:
        print 'Congratulations, you are right. You use %d times to get it.' % count
        break
    elif guess < randNum:
        print 'No, it\'s a liitle lower than that.'
    else:
        print 'No, it\'s a little higher than that.'