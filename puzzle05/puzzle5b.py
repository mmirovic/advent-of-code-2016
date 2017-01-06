#!/usr/bin/python
# Advent of code 2016 by mmirovic

import hashlib
import sys, signal, os
import threading

def signal_handler(signal, frame):
    print '\nTerminated at iteration %d' % i
    os._exit(1)
#	sys.exit(1)	
	

signal.signal(signal.SIGINT, signal_handler)

key = "reyedfim"
l = 5
i = 0
code = ['.']*8
animation = '|/-\\|/-\\'

def next_hash(txt,i):
 	while hashlib.md5(txt+str(i)).hexdigest()[0:l] != '0'*l:
		i +=1
	return [hashlib.md5(txt+str(i)).hexdigest(), i+1]

def animate():
	global animation
	txt = ''.join(code)
	animation = animation[1:]+animation[0]
	txt = txt.replace ('.', animation[0])
	sys.stdout.write('\r' + txt )
	sys.stdout.flush()
	if '.' in code:
		t = threading.Timer(0.5,animate)
		t.start()
	else:
		print '\nDone'

animate()

while '.' in code: 
	[hash, i] = next_hash(key,i)
	index = int(hash[5]) if hash[5].isdigit() else -1
	if index >= 0 and index <=7 and code[index] == '.':
		code[index] = hash[6]    
