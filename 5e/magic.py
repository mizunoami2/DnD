#!/usr/bin/env python
from sys import argv


class Caster(object):
	def __init__(self, name, levels):
		self.name = name
		self.spells = ['' for i in range(levels)]
		self.slots = ['' for i in range(levels)]

	def printCaster(self):
		print "Caster name: %s" % (self.name)
		for k in range(len(self.spells)):
			print "k is %i" % (k)
			if self.slots[k] == 99:
				print "Cantrips: "
			else:
				print "Level %i spells (%i slots left):" % (k, self.slots[k])
			for j in range(len(self.spells[k])):
				print self.spells[k][j]
			print
		print


if len(argv) > 1:
	fName = argv[1]
else:
	fName = 'party.mgc'
file = open(fName, 'r+')
nCasters = int(file.readline())
casters = ['' for i in range(nCasters)]
for i in range(nCasters):
	name = file.readline().rstrip()
	levels = int(file.readline())
	casters[i] = Caster(name, levels)

	for k in range(levels):
		numSpells = int(file.readline())
		casters[i].spells[k] = ['' for alpha in range(numSpells)]
		for alpha in range(numSpells):
			casters[i].spells[k][alpha] = file.readline().rstrip()
	for k in range(levels):
		casters[i].slots[k] = int(file.readline())
	casters[0].printCaster()