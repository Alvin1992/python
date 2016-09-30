#!/usr/bin/python
# Filename: if.py
number = 23
guess = int(raw_input('Enter an interger : '))

if guess == number:
    print 'Congrats, you guessed it.'
    print '(but you do not with any prizes!)'
elif guess < number:
    print 'No, it is a little higher than that'
else:
    print 'No, it is a little lower than that'

print 'Done'