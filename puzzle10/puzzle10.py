#!/usr/bin/python
# Advent of code 2016 by mmirovic


bots = {}
output = {}
	
f = open('input', 'r')

for l in f:
	i = l.split()

	# value 61 goes to bot 119
	if i[0] == 'value':
		i[1], i[5] = int(i[1]), int(i[5])
	
		if i[5] not in bots:
			bots[i[5]] = set([])
	
		bots[i[5]].add(i[1])
	
def one_round():

	global bots, output, f

	f.seek(0)
	for l in f:
		i = l.split()
		
		
		#bot 177 gives low to output 8 and high to bot 157
		#bot 26 gives low to bot 131 and high to bot 149
		if i[0] == 'bot' and int(i[1]) in bots and len(bots[int(i[1])]) == 2:
									
			i[1], i[6], i[11] = int(i[1]), int(i[6]), int(i[11])
			
			if min(bots[i[1]]) == 17 and max(bots[i[1]]) == 61:
				print "Found bot giving 17 and 61:", i[1]
		
			if i[5] == 'output':	
				output[i[6]] = min(bots[i[1]])				
		
			if i[5] == 'bot':
				if i[6] not in bots:
					bots[i[6]] = set([])
				bots[i[6]].add(min(bots[i[1]]))
				
			if i[10] == 'output':
				output[i[11]] = max(bots[i[1]])				
		
			if i[10] == 'bot':
				if i[11] not in bots:
					bots[i[11]] = set([])	
				bots[i[11]].add(max(bots[i[1]]))

			# remove both elements
				bots[i[1]] = set([])

while True:		
	one_round()
	if 0 in output and 1 in output and 2 in output:
		print "Output 0*1*2=", output[0]*output[1]*output[2]
		break
