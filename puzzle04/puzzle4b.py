#!/usr/bin/python

f = open('input', 'r')

def shift(str, value):
	res = ''
	shift = value % 26
	for c in str:
		n = ord (c) - 97
		n = (n + value) % 26 + 97
		res += chr(n)
	return res 

def decypher(list, value):
	res = []
	for i in list:
		res += [shift(i, value)]
	return res

for l in f:
	str = l.strip().replace('[','-').replace(']','').split('-')
	
	message = ' '.join( decypher (str[:-2],int(str[-2])) )
	
	if 'object' in message:
		print message, str[-2]
