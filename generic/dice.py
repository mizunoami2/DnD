#!/usr/bin/env python
from random import randint

total = 0;
number = int(raw_input("How may dice are you rolling: "))
size = int(raw_input("How many sides on the dice: "))
mod = int(raw_input("What is the total modifier: "))
i = 0
roll = 0
while i < number:
	roll = randint(1,size)
	print "Die number %2s: %i" % (i+1, roll)
	total += roll
	i += 1
total += mod
if mod >= 0:
	print "%id%i+%i: %i" % (number, size, mod, total)
else:
	print "%id%i%i: %i" % (number, size, mod, total)