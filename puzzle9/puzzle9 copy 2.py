#!/usr/bin/python
# Advent of code 2016 by mmirovic

import os

#l = open('input', 'r').read().strip()
#l = "A(2x2)BCD(2x2)EFG"
#l = "X(8x2)(3x3)ABCY"
#l = "(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN"
l = "(27x12)(20x12)(13x14)(7x10)(1x12)A"

def decomp (f_input,f_output):

	l = open(f_input, 'r')
	r = open(f_output, 'w')
	end = True

	while l.tell() < os.stat(f_input).st_size:

		d = l.read(1)
		if d == '(':
			
			while d[-1] != ')':
				d += l.read(1)

			size = d.replace('(','').replace(')','').split('x')
			size = [ int(size[0]), int(size[1]) ]
			r.write(size[1]*l.read(size[0]))
			end = False
	
		else:
			r.write(d)

	l.close()
	r.close()
	return end
	

print decomp ('output0','output1')
counter = 1

while decomp ('output'+str(counter),'output'+str(counter+1)) != True:
	print counter
	counter += 1




