#!/usr/bin/python
# Advent of code 2016 by mmirovic

import hashlib

move = {'U': [0,-1], 'D':[0,1], 'L':[-1,0], 'R':[1,0]}
open = 'bcdef'
dirs = 'UDLR'

def bfs(key):
	queue = [[key, [0,0]]]
	length = 0
	while queue:
		[path, pos] = queue.pop(0)
		hash = hashlib.md5(path).hexdigest()[:4]
		doors = [c for i, c in enumerate(dirs) if hash[i] in open]

		for d in doors:
			pos2 = [pos[0]+move[d][0], pos[1]+move[d][1]]
			if not (0 <= pos2[0] <=3 and 0 <= pos2[1] <= 3):
				continue
			elif pos2 == [3,3]:
				length = len(path[8:])+1
			else:
				queue.append([path+d, pos2])
	return length

#key = 'ulqzkmiv'
#key = 'ihgpwlah'
key = 'vkjiggvb'
print bfs(key)
