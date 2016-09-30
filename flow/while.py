#!/usr/bin/python
# Filename: while.py
num = 23
running = True

while running:
    guess = int(raw_input('Enter an integer : '))

    if guess == num:
        print "congratulations, you guessed it."
        running = False
    elif guess < num:
        print "No, it's a little higher than that"
    elif guess > num:
        print "No, it's a little lower than that"
else:
    print "The whole loop is over."

print 'Done'