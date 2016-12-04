#!/usr/bin/python

f = open('input', 'r')

i = 0

def triangle (sides):
	s = sorted(map(int,sides.split()))
	if s[0] + s[1] > s[2]:
		return True
	else:
		return False
		
for l in f:
	if triangle(l):
		i += 1

print "Number of triangles", i