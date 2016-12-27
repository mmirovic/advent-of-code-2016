#!/usr/bin/python
# Advent of code 2016 by mmirovic

import itertools

f = open('input', 'r')

#s = 'abcde'
s = 'abcdefgh'
res = 'fbgdceah'

prg = []
for l in f:
	prg += [l.strip()]

def cmd(l,s):

	#print l
	i = l.split()
	
	# move position 2 to position 1
	if i[0] == 'move':
		i[2], i[5] = int(i[2]), int(i[5])
			
		t = s[i[2]]
		s = s[:i[2]] + s[i[2]+1:]
		s = s[:i[5]] + t + s[i[5]:]
		
	# swap position 0 with position 4
	if i[0] == 'swap' and i[1] == 'position':
		i[2], i[5] = int(i[2]), int(i[5])
		if i[2] > i[5]:
			i[2], i[5] = i[5], i[2]
		s = s[:i[2]] + s[i[5]] + s[i[2]+1:i[5]] + s[i[2]] + s[i[5]+1:]

	# swap letter d with letter a		
	if i[0] == 'swap' and i[1] == 'letter':
		t1, t2 = i[2], i[5]
		s = s.replace(t2,'X')
		s = s.replace(t1,t2)
		s = s.replace('X',t1)

	# reverse positions 1 through 6
	if i[0] == 'reverse':
		i[2], i[4] = int(i[2]), int(i[4])
		s = s[:i[2]] + s[i[2]:i[4]+1][::-1] + s[i[4]+1:]

	if i[0] == 'rotate':

		# rotate left 6 steps 
		if i[1] == 'left':
			i[2] = int(i[2])		
			s = s[i[2]:] + s[:i[2]]	
		elif i[1] == 'right':
			i[2] = int(i[2])
			i[2] = len(s) - i[2]
			s =  s[i[2]:] + s[:i[2]]

		# rotate based on position of letter a		
		else:
			c = 1 + s.find(i[6]) + (1 if s.find(i[6]) >= 4 else 0)
			c = len(s) - c	
			s = s[c:] + s[:c]

	#print s, '\n'
	return s
	
def pwd(s):

	for l in prg:	
		s = cmd(l,s)		
	
	return s


for a in itertools.permutations(s):
	if pwd(''.join(a)) == res:
		print ''.join(a)
		break
		
		
	


	