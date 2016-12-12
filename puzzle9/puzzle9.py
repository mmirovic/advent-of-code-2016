#!/usr/bin/python
# Advent of code 2016 by mmirovic

l = open('input', 'r').read().strip()

def decomp (l, level):

	size = 0
	c = 0
	
	while c < len(l):
	
		if level <= 1:
			print c, level

		if l[c] == '(':
			s = l[ c+1 : c+l[c:].index(')') ].split('x')
			s = [ int(s[0]), int(s[1]) ]

			c += l[c:].index(')') + 1
			
			size += decomp(l[ c : c+s[0] ]*s[1], level+1)
			c += s[0]
 
		else:
			size += 1
			c += 1
	
	return size
	

print decomp (l, 0)


