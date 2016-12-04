#!/usr/bin/python

import collections as col

f = open('input', 'r')
c = 0 # count

def find_hash(str):
	res = col.Counter(str)
	res = sorted(res.items(), key=lambda pair: (-pair[1], pair[0]))
	res = list(c[0] for c in res)
	return ''.join(res)[:5]

for l in f:
	str = l.strip().replace('[','-').replace(']','').split('-')
	if find_hash(''.join(str[:-2])) == str[-1]:
		c += int(str[-2])

print "Total sum is", c
