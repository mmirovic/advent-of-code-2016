#!/usr/bin/python

import math, numpy as np

str = open('input1', 'r').read().replace(',','').split()

direction = math.pi / 2 # facing north
a = np.zeros((512,512)) # map of the place, in matrix form
pos = [128,128]

for i in str:

	direction += math.pi/2 * ( 1 if i[0] == 'L' else -1 )
	pos2 = [ pos[0] + int(round(math.cos(direction) * int(i[1:])))  , pos[1] + int(round(math.sin(direction) * int(i[1:]))) ]

	a[ min(pos,pos2)[1] : max(pos,pos2)[1]+1 , min(pos,pos2)[0] : max(pos,pos2)[0]+1 ] += 1
	a[ pos[1],pos[0] ] -= 1

	pos = pos2

	if len(np.nonzero(a==2)[0]) == 1:	
		print "Location is:", np.nonzero(a==2)[0][0]-128 + np.nonzero(a==2)[1][0]-128
		break
	
