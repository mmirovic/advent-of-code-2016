#!/usr/bin/python

import collections as col

def most_common(list, el):
	res = ''
	for line in list:
		res += col.Counter(line).most_common(26)[el][0]
	return res
		
# load file into a list
f = open('input', 'r')
input = []
for l in f:
	input += [l.strip()]
	
# transpose list
trans = []
for i in range(len(input[0])):
	trans += [''.join(list(line[i] for line in input))]

# find most/least common; 0 for most common, -1 for least common
print most_common(trans,-1)
