#!/usr/bin/python

f = open('input', 'r')

pos = [1,1]
dir = { "L":[-1,0], "R":[1,0], "U":[0,-1], "D":[0,1]}
ans = []
dim = 3

def update_pos (p,char):
	return [ min(max(0, p[0] + dir[c][0]),dim-1) , min(max(0, p[1] + dir[c][1]),dim-1) ]

def pos_to_key (pos):	
	return pos[1]*dim + pos[0]+1

for l in f:
	for c in l.strip():
		pos = update_pos(pos,c)
	ans += [pos_to_key(pos)]
		
print "Code is", ans
