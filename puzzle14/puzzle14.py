#!/usr/bin/python
# Advent of code 2016 by mmirovic

import hashlib

salt = "cuanljph"
#salt = "abc"

keys = 0
f = {}

def find(s,l):
	for i in range(len(s)+1-l):
		if s[i]*l == s[i:i+l]:
			return s[i]
	return False

i = 0
while keys < 64:

	hash  = salt+str(i)
	
	for c in range(2017):
		hash = hashlib.md5(hash).hexdigest()
	
	if find(hash,5) != False and find(hash,5) in f:

		for t in f[find(hash,5)]:
			if t + 1000 >= i:
				keys += 1
				print hash, t, i, keys

			f[find(hash,5)] = []	
				
	if find(hash,3) != False:
		if find(hash,3) not in f:
			f[find(hash,3)] = [i]
		else:
			f[find(hash,3)] += [i]

	i += 1
