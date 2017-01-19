#!/usr/bin/python
# Advent of code 2016 by mmirovic

f = open('input', 'r').read().strip()
#size = 40
size = 400000

traps = {'^^.':'^', '.^^':'^', '^..':'^', '..^':'^'}

map = ['.' + f + '.']
for r in range(size-1):

	# new row
	map += ['.']
	for i in range(len(map[0])-2):
		map[r+1] += traps.get(map[r][i:i+3],'.')
	map[r+1] += '.'

# reduce by size*2 - imaginary correct values
print ''.join(map).count('.')-size*2
