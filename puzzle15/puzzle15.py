#!/usr/bin/python
# Advent of code 2016 by mmirovic

import sys

# read the disc locations
f = open('input', 'r')
loc, size = [], []
for l in f:
	loc  += [int(l.split()[11][:-1])]
	size += [int(l.split()[3])]

# extra element for part b
loc  += [0]
size += [11]

# align the time shift to reach all the discs
loc = [i+c+1 for c, i in enumerate(loc)]

t = 0
while sum(loc) != 0:
	loc = [(loc[i]+1)%size[i] for i in range(len(loc))]
	t += 1
	sys.stdout.write('\r' + str(loc))
	
print '\nTime is', t
