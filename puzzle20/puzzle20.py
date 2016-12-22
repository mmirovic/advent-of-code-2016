#!/usr/bin/python
# Advent of code 2016 by mmirovic

f = open('input', 'r')

ranges = []
for l in f:
	ranges += [[int(c) for c in l.strip().split('-')]]
	
ranges = sorted(ranges, key=lambda tup: tup[0])
ranges += [[2**32]]

ip, adr = 0, 0

for i in range(len(ranges)-1):
	if ip < ranges[i][1]:
		ip = ranges[i][1]
	
	if ip < ranges[i+1][0]:
		adr += ranges[i+1][0] - ip - 1
		ip = ranges[i+1][0]
		print ip, adr
