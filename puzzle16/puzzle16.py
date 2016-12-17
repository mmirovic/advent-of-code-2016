#!/usr/bin/python
# Advent of code 2016 by mmirovic


class Dragon:

	def __init__(self, init, size):
		self.val = [int(c) for c in init]
		self.size = size

	def expand(self):
		while len(self.val) < self.size:
			self.val += [0] + [not i for i in self.val[::-1]]

		self.val = self.val[:self.size]
		return self.val
			
	def checksum(self):

		while len(self.val)%2 != 1:
			csum = []
			for i in range(len(self.val)/2):
					csum += [1] if self.val[i*2] == self.val[i*2+1] else [0]
			self.val = csum
			
		return self.val


init = '11100010111110100'
#size  = 272
size = 35651584

data = Dragon(init, size)
data.expand()
print ''.join(str(c) for c in data.checksum())
