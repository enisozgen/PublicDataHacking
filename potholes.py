#!/usr/bin/python2.7

import csv

potholes_by_block = { }


def make_block(address):
    '''
    Rewrite an address to strip address to 1000's (10 blocks\
    )'''
    parts = address.split()
    # For a number like '5412' this makes '5XXX'
    parts[0] = parts[0][:-3] + 'XXX'
    return ' '.join(parts)

f = open('potholes.csv')
for row in csv.DictReader(f):
    status = row['STATUS']
    if status == 'Open':
        addr = row['STREET ADDRESS']
        num = row['NUMBER OF POTHOLES FILLED ON BLOCK']
    
    # Tabulate
    block = make_block(addr)
    if block not in potholes_by_block:
        #This is the first occurence of given adress \

        potholes_by_block[block] = 1
    else:
        potholes_by_block[block] += 1


# Problem: how to sort, find most potholes?
num_potholes_block = []
for key in potholes_by_block.keys():
    num_potholes_block.append((potholes_by_block[key],
                               key))

num_potholes_block.sort(reverse=True )
for num, block in num_potholes_block[:10]:
    print num, block

# other thing written on the video
# python2.7 mode
# >>> f = open('potholes.csv')
# >>> import csv
# >>> r = csv.DictReader(f)
# >>> next(r)
