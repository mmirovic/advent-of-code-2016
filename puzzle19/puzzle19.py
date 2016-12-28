#!/usr/bin/python
# Advent of code 2016 by mmirovic

c = 3018458
#c = 5

type = 2

class Table:

	def __init__(self,c):
		self.table = range(1,c+1)
		
	def tour(self):

		i = 0
		while i < len(self.table):
			if self.table[i] != 0:
				self.table[(i+1)%len(self.table)] = 0
			i += 1
		
		# remove 0 elements
		self.table = [e for e in self.table if e > 0]
		
		while len(self.table) >= 2:
			print len(self.table)
			self.tour()		
		
		return self.table
		
	def tour2(self):
		
		i = 0
		while i < len(self.table):
			s = len(self.table)
			o = (i + s/2) % s
			del self.table[o]
			if o > i:
				i += 1
			
			if i%50000 == 0:
				print "*", i
							
		while len(self.table) >= 2:
			print len(self.table)
			self.tour2()		
		
		return self.table
		

table = Table(c)
if type == 1:
	print table.tour()
else:
	print table.tour2()
	
