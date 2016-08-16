#!/usr/bin/env python
from random import randint

total = 0;
number = int(raw_input("How may dice are you rolling: "))
size = int(raw_input("How many sides on the dice: "))
mod = int(raw_input("What is the total modifier: "))
i = 0
while i < number:
	total += randint(1,size)
	i += 1
total += mod
if mod >= 0:
	print "%id%i+%i: %i" % (number, size, mod, total)
else:
	print "%id%i%i: %i" % (number, size, mod, total)