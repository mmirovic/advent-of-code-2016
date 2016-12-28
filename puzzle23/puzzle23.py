#!/usr/bin/python
# Advent of code 2016 by mmirovic


def is_int(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

class Cpu:
	
	def __init__(self, file='input'):
		self.reg = {'a':12, 'b':0, 'c':0, 'd':0}
		self.pc = 0
		self.tgl = {'inc':'dec', 'jnz':'cpy', 'cpy':'jnz', 'dec':'inc', 'tgl':'inc'}
	
		# read in the program
		f = open(file, 'r')
		self.prg = []
		for l in f:
			self.prg += [l.strip()]
	
	
	def ins(self):
		ins = self.prg[self.pc].split()


		'''
		inc a
		dec c
		jnz c -2
		dec d
		jnz d -5
		'''
		
		if ins[0] == 'inc' and ins[1] == 'a':
			self.reg['a'] = self.reg['a'] + self.reg['c']*self.reg['d']
			self.reg['c'] = 0
			self.reg['d'] = 0

			self.pc += 5
			return			

		if ins[0] == 'cpy' and not is_int(ins[2]):
			self.reg[ins[2]] = int(ins[1]) if is_int(ins[1]) else self.reg[ins[1]]

		if ins[0] == 'inc':
			self.reg[ins[1]] += 1

		if ins[0] == 'dec':
			self.reg[ins[1]] -= 1
				
		if ins[0] == 'jnz' and (int(ins[1]) if is_int(ins[1]) else self.reg[ins[1]]) != 0:
			self.pc += int(ins[2]) if is_int(ins[2]) else self.reg[ins[2]]			
			return
			
		if ins[0] == 'tgl' and  0 <= (self.pc + self.reg[ins[1]]) < len(self.prg):
			t_pc = self.pc + self.reg[ins[1]]
			t_ins = self.prg[t_pc].split()
			
			self.prg[t_pc] = self.tgl[t_ins[0]] + self.prg[t_pc][3:]
	
		self.pc += 1
		
	def val(self):
		return self.pc, self.reg, (True if self.pc < len(self.prg) else False)

if __name__ == '__main__':
	
	cpu = Cpu()

	while cpu.val()[2]:
		cpu.ins()
#		print cpu.val()

	print cpu.val()[1]
