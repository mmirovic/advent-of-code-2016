#!/usr/bin/python
# Advent of code 2016 by mmirovic

import itertools as it
part = 2

class Maze:

	def __init__ (self, file='input'):
	
		self.maze = {}
		self.visit = []
		self.start = ()

		f = open(file, 'r')
		y = 0
	
		for y, l in enumerate(f):
			l = l.strip()
			for x, c in enumerate(l):
				self.maze[(x,y)] = c
				try:
					if int(c) == 0:
						self.start = (x,y)
					else:
						self.visit += [(x,y)]
				except:
					pass
					
		self.size = [ x+1, y+1 ]
					
	def __str__(self):

		res = ''

		for y in range(self.size[1]):
			for x in range(self.size[0]):
				res += self.maze[(x,y)]
			res += '\n'	

		return res

	def shortest_path(self):
		length = 10000
		
		spf = {}
		for v in [self.start] + self.visit:
			spf[v] = self.dijkstra(v)
			print 'SPF of', v, 'done.'
		
		
		for path in it.permutations(self.visit):
			l = 0
			path = (self.start,) + path

			if part == 2:
				path += (self.start,)

			for el in range(len(path)-1):
				l += spf[path[el]][path[el+1]][0]
				
			length = min( length, l)

		return length

	def neighbor(self, pos):
		queue = []

		for x, y in [[pos[0]-1,pos[1]], [pos[0]+1,pos[1]], [pos[0],pos[1]-1], [pos[0],pos[1]+1]]:
			try:
				if self.maze[(x,y)] != '#':
					queue += [(x,y)]
			except:
				pass
		return queue	
			
					
	def dijkstra(self, start):
	
		max = 1000000
		
		spf = {}
		Q = {}
		
		for y in range(self.size[1]):
			for x in range(self.size[0]):	
				spf[(x,y)] = [max, None]
				Q[(x,y)] = max
		
		spf[start][0] = 0
		Q[start] = 0
		
		while len(Q) != 0:
			u = min(Q, key=Q.get)
			del Q[u]
			
			for v in self.neighbor(u):
				alt = spf[u][0] + 1
				if alt < spf[v][0]:
					spf[v][0] = alt
					Q[v] = alt
					spf[v][1] = u
									
		return spf

maze = Maze('input')
#print maze
print maze.shortest_path()