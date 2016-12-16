#!/usr/bin/python
# Advent of code 2016 by mmirovic


def is_int(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

class Cpu:
	
	def __init__(self):
		self.reg = {'a':0, 'b':0, 'c':1, 'd':0}
		self.pc = 0
	
	def ins(self, ins):
		ins = ins.split()

		if ins[0] == 'cpy':
			self.reg[ins[2]] = int(ins[1]) if is_int(ins[1]) else self.reg[ins[1]]

		if ins[0] == 'inc':
			self.reg[ins[1]] += 1

		if ins[0] == 'dec':
			self.reg[ins[1]] -= 1
		
		if ins[0] == 'jnz' and (int(ins[1]) if is_int(ins[1]) else self.reg[ins[1]]) != 0:
			self.pc += int(ins[2])
			return		
		
		self.pc += 1
		
	def val(self):
		return self.pc, self.reg

if __name__ == '__main__':
	
	# read in the program
	f = open('input', 'r')
	prg = []
	for l in f:
		prg += [l.strip()]

	cpu = Cpu()

	while cpu.val()[0] < len(prg):
		cpu.ins(prg[cpu.val()[0]])
#		print cpu.val()

	print cpu.val()[1]
