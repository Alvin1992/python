#!/usr/bin/python
# Filename: using_dict.py

# 'ab' is short for 'a'ddress'b'ook

ab = {
    'Alvin': 'fanrx_1992@163.com',
    'Kathy': 'kathy@163.com'
}

print 'Alvin\'s address is %s' % ab['Alvin']

# Adding a key/value pair
ab['Kate'] = 'Kate@163.com'

# Deleting a key/value pair
del ab['Kathy']

print '\nThere are %d contacts in the address-book\n' % len(ab)
for name, address in ab.items():
    print 'Contact %s at %s' % (name, address)

if 'Kate' in ab:
    print '\nKate\'s address is %s' % ab['Kate']