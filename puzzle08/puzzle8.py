#!/usr/bin/python
# Advent of code 2016

import numpy as np

s = np.zeros((6,50),dtype=np.int)

# load the file
f = open('input', 'r')
for l in f:
	man = l.strip().split()

	if man [0] == 'rect':
		d = man[1].split('x')
		d = [int(el) for el in d]
	
		# fill in the matrix
		s[ :d[1] , :d[0] ] = 1
	
	if man[0] == 'rotate' and man[1]=='row':
		s[int(man[2][2:]),:] = np.roll(s[int(man[2][2:]),:],int(man[4]))

	if man[0] == 'rotate' and man[1]=='column':
		s[:,int(man[2][2:])] = np.roll(s[:,int(man[2][2:])],int(man[4]))
	
print

for l in range(6):
	txt = [str(c) for c in s[l,:]]
	print ''.join(txt).replace('0',' ').replace('1','X')

print '\nLit pixels', int(s.sum())
