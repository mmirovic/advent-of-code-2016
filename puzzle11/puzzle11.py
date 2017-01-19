#!/usr/bin/python
# Advent of code 2016 by mmirovic

f = open('input', 'r')
		
floor = []
steps = 0
part = 2

for l in f:
	el = 0
	l = l.split(' a ')
	for w in l:
		if 'generator' in w or 'microchip' in w:
			el += 1
	floor += [el]

if part == 2:
	floor[0] += 4

for f in range(4-1):
	steps += 1 + (floor[f]-2)*2
	floor[f+1] += floor[f]
	floor[f] = 0

print floor, steps
