#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Filename: objvar.py


class Person:
    """Represent a person."""
    population = 0

    def __init__(self, name):
        """Initializes the person's data."""
        self.name = name
        print 'Initializing %s' % self.name

        # 当创建了一个人时，加到总人口中
        Person.population += 1

    def __del__(self):
        """I'm dying."""
        print '%s says bye.' % self.name

        Person.population -= 1

        if Person.population == 0:
            print 'I\'m the last one.'
        else:
            print 'There are still %d people left.' % Person.population

    def sayHi(self):
        """Greeting by the person.

        Really that's all it does"""

        print 'Hi, my name is %s' % self.name

    def howMany(self):
        """Print the current population."""
        if Person.population == 1:
            print 'I\'m the only person here.'
        else:
            print 'We have %d persons here' % Person.population

alvin = Person('Alvin')
alvin.sayHi()
alvin.howMany()

kathy = Person('Kathy')
kathy.sayHi()
kathy.howMany()

alvin.sayHi()
alvin.howMany()
