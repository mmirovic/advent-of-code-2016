#!/usr/bin/python
# Advent of code 2016 by mmirovic

import hashlib
import sys
import signal

def signal_handler(signal, frame):
        print '\nTerminated at iteration %d' % i
        sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

key = "reyedfim"

#l = input ("How many 0's in the hash? ")
l = 5

i = 0
code = ''

while len(code) <= 7: 
	hash = hashlib.md5(key+str(i)).hexdigest()
	if hash[0:l] == '0'*l :
		code += hash[5]
		sys.stdout.write('\r' + code + (8-len(code))*'.' )
		sys.stdout.flush()
	i += 1

print "Done"
