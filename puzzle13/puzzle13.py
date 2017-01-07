#!/usr/bin/python
# Advent of code 2016 by mmirovic

import numpy as np

#input = 10
input = 1352
start = (1,1)
#end = (4,7)
end = (39,31)
size = (50,50)
max_len = 50

class Maze:

	def __init__(self, input, size):
		self.m = np.zeros(size,dtype=np.int)
		
		for y in range(self.m.shape[0]):
			for x in range (self.m.shape[1]):
				self.m[y,x] = 1 if bin(x*x + 3*x + 2*x*y + y + y*y + input).count('1') % 2 == 1 else 0

	def __str__(self):
	
		res = ''		
		for l in range(self.m.shape[0]):
			txt = [str(c) for c in self.m[l,:]]
			res += ''.join(txt).replace('0','.').replace('1','#').replace('2','O') + '\n'
		return res
		
	def draw(self,path):
		for e in (path):
			self.m[e] = 2	

	def opt(self, pos):
		queue = []

		for y, x in [[pos[0]-1,pos[1]], [pos[0]+1,pos[1]], [pos[0],pos[1]-1], [pos[0],pos[1]+1]]:
			try:
				if self.m[y,x] == 0:
					queue += [(y,x)]
			except:
				pass
		return queue

	# Breadth-First Search
	def bfs(self, start, end, max_len = -1):
		
		queue = [(start, [])]
		while queue:
			(vertex, path) = queue.pop(0)
			for next in set(self.opt(vertex)) - set(path):
				if next == end:
					yield path + [next]
				elif len(path) == max_len:
					yield None
				else:
					queue.append((next, path + [next]))

	def val(self,e):
		return self.m[e]

maze = Maze(input,size)
part = 2

if 	part == 1:
	spf = maze.bfs(start,end).next()
	print len(spf)
	maze.draw(spf)
	print maze
else:
	print len( [(y,x) for y in range(50) for x in range(50) if maze.val((y,x)) == 0 and maze.bfs(start,(y,x),max_len).next() != None] )
