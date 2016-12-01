#!/usr/bin/python

import math

str = open('input1', 'r').read().replace(',','').split()

direction = math.pi / 2 # facing north
pos = [0,0]

for i in str:
	direction += math.pi/2 * ( 1 if i[0] == 'L' else -1 )
	pos = [ pos[0] + math.cos(direction) * int(i[1:]) , pos[1] + math.sin(direction) * int(i[1:]) ]
	
print "Distance is:", int(pos[0]+pos[1])
