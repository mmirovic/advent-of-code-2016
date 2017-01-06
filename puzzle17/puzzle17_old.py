#!/usr/bin/python
# Advent of code 2016 by mmirovic

import hashlib
import sys

class Maze:

	def __init__ (self, key):
		self.options = [key]
		self.length = 0
		
		self.vault = [3,3]
		self.move = {'U': [0,-1], 'D':[0,1], 'L':[-1,0], 'R':[1,0]}
		# Any b, c, d, e, or f means that the corresponding door is open...
		self.open = 'bcdef'
		self.doors = 'UDLR'
		
	def end_pos(self, s):
		pos = [0,0]
		for c in s[8:]:
			pos = [pos[0]+self.move[c][0], pos[1]+self.move[c][1]]

		if 0 <= pos[0] <= 3 and 0 <= pos[1] <= 3:
			return pos
		else:
			return False
	
	def check(self):
		
		options = []
		for key in self.options:
			
			for j in range(4):
				hash = hashlib.md5(key).hexdigest()
				if hash[j] in self.open and self.end_pos(key+self.doors[j]) != False:
					if self.end_pos(key+self.doors[j]) == self.vault:
						self.length = len((key+self.doors[j])[8:])
					else:
						options += [key+self.doors[j]]
				
		self.options = options			
		return self.length

key = 'vkjiggvb'
#key = 'ihgpwlah'
maze = Maze(key)

while True: 
	print maze.check()
