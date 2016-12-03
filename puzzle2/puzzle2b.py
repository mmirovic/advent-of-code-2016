#!/usr/bin/python

f = open('input', 'r')

pos = [0,2]
dir = { "L":[-1,0], "R":[1,0], "U":[0,-1], "D":[0,1]}
map = { (2,0):'1', (1,1):'2', (2,1):'3', (3,1):'4', (0,2):'5', (1,2):'6', (2,2):'7', (3,2):'8', (4,2):'9', (1,3):'A', (2,3):'B', (3,3):'C', (2,4):'D' } 
ans = []
dim = [(2,2),(1,3),(0,4),(1,3),(2,2)] # dimensions by line

def update_pos (p,char):
	r = []
	r += [ min(max(dim[p[1]][0], p[0] + dir[c][0]),dim[p[1]][1]) ]
	r += [ min(max(dim[p[0]][0], p[1] + dir[c][1]),dim[p[0]][1]) ]
	return r

def pos_to_key (pos):	
	return map[(pos[0],pos[1])]

for l in f:
	for c in l.strip():
		pos = update_pos(pos,c)
		print pos, c
	ans += [pos_to_key(pos)]
		
print "Code is", ans
