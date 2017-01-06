#!/usr/bin/python
# Advent of code 2016 by mmirovic

import re

word_count = 0
puzzle = 2

def has_abba(lst):
	for str in lst:
		for i in range(len(str)-3):
			if str[i] == str[i+3] and str[i+1] == str[i+2] and str[i] != str[i+1]:
				return True
	return False

def aba_set(lst):
	res = set([])
	for str in lst:
		for i in range(len(str)-2):
			if str[i] == str[i+2] and str[i] != str[i+1]:
				res.add(str[i:i+3])
	return res
	
def aba_to_bab(aba):
	res = set([])
	for el in aba:
		res.add(el[1]+el[0]+el[1])
	return res
	
def check_bab(lst,bab):
	for str in lst:
		for el in bab:
			if el in str:
				return True
	return False
		

# load file and break it in words

f = open('input', 'r')
for l in f:
	# break into words
	input = re.findall(r"[\w']+", l)

	# first part of the puzzle
	if puzzle == 1:
		# odd words must have 'abba'

		if has_abba(input[0::2]) and not has_abba(input[1::2]):
			word_count += 1

	# second part of the puzzle
	if puzzle == 2:
		aba, bab = set([]), set([])
		aba = aba_set(input[0::2])
		bab = aba_to_bab(aba)
		if check_bab(input[1::2],bab):
			word_count += 1
	
print "Resolving puzzle part", puzzle
print "Result", word_count
