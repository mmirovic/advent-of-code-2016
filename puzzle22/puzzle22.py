#!/usr/bin/python
# Advent of code 2016 by mmirovic

import itertools

class Grid:

	def __init__(self,file='input'):
		self.nodes = {}

		# read in the grid
		f = open(file, 'r')
		
		'''
		root@ebhq-gridcenter# df -h
		Filesystem              Size  Used  Avail  Use%
		/dev/grid/node-x0-y0     85T   65T    20T   76%
		'''
		
		# skip first two lines
		f.readline()
		f.readline()
		
		for l in f:
			l = l.split()
			coord = tuple([ int(c) for c in l[0][15:].replace('x','').replace('y','').split('-') ])
			self.nodes[coord] = [ int(l[1][:-1]), int(l[2][:-1]) ]
			if self.nodes[coord][1] == 0:
				self.empty = coord

		self.size = [ c+1 for c in coord]

	
	def __str__(self):

		spf = self.shortest((self.size[0]-2,0))
		l = ''

		for y in range(self.size[1]):
			for x in range(self.size[0]):
				if self.nodes[(x,y)][1] == 0:
					l += '_'
				elif self.nodes[(x,y)][0] > 500:
					l += '#'
				elif (x,y) in spf:
					l += 'O'
				else:
					l += '.'
			l += '\n'		

		return l
	
		
	def viable(self):
	
		'''
		Node A is not empty (its Used is not zero).
		Nodes A and B are not the same node.
		The data on node A (its Used) would fit on node B (its Avail).
		'''
	
		c = 0
		keys = [k for k in self.nodes]
		for a in itertools.permutations(keys,2):	
			if self.nodes[a[0]][1] != 0 and self.nodes[a[0]][1] <= (self.nodes[a[1]][0]-self.nodes[a[1]][1]):
				c += 1
	
		return c
		
	def data_move(self):
		self.dijkstra(self.empty)
		return self.spf[(35,0)][0] + 5*35 + 1
			
	def neighbor(self, pos):
		queue = []

		for x, y in [[pos[0]-1,pos[1]], [pos[0]+1,pos[1]], [pos[0],pos[1]-1], [pos[0],pos[1]+1]]:
			try:
				if self.nodes[(x,y)][0] < 100:
					queue += [(x,y)]
			except:
				pass
		return queue	
			
					
	def dijkstra(self, start):
	
		max = 1000000
		
		self.spf = {}
		Q = {}
		
		for y in range(self.size[1]):
			for x in range(self.size[0]):	
				self.spf[(x,y)] = [max, None]
				Q[(x,y)] = max
		
		self.spf[start][0] = 0
		Q[start] = 0
		
		while len(Q) != 0:
			u = min(Q, key=Q.get)
			del Q[u]
			
			for v in self.neighbor(u):
				alt = self.spf[u][0] + 1
				if alt < self.spf[v][0]:
					self.spf[v][0] = alt
					Q[v] = alt
					self.spf[v][1] = u
									
		return
	
	def shortest(self, end):
		path = []
		u = end
		while self.spf[u][1] != None:
			path += [u]
			u = self.spf[u][1]
	
		return path
		
		
		
part = 2						
grid = Grid()

if part == 1:
	print grid.viable()
else:
	print grid.data_move()
	print grid



