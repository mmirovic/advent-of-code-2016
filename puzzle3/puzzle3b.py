#!/usr/bin/python

f = open('input', 'r')
l = f.read().split()
i = 0

def triangle (sides):
	s = sorted(map(int,sides))
	if s[0] + s[1] > s[2]:
		return True
	else:
		return False

c = 0
while c < len(l):
	for j in range (3):
		if triangle([l[c+j],l[c+j+3],l[c+j+6]]):
			i += 1
	c += 9

print "Number of triangles", i