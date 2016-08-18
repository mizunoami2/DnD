#!/usr/bin/env python
from sys import argv


class Caster(object):
	def __init__(self, name, levels):
		self.name = name
		self.spells = ['' for i in range(levels)]
		self.slots = ['' for i in range(levels)]

	def printCaster(self):
		print "\nCaster name: %s" % (self.name)
		for k in range(len(self.spells)):
			o = k
			if self.slots[0] != 99:
				o += 1
			if self.slots[k] == 99:
				print "Cantrips: "
			else:
				print "Level %i spells (%i slots left):" % (o, self.slots[k])
			for j in range(len(self.spells[k])):
				print self.spells[k][j]
			print

	def removeSpell(self, level, name):
		if name in self.spells[level]:
			self.spells[level].remove(name)
		else:
			print "%s doesn't know %s." % (self.name, name)

	def addSpell(self, level, name):
		if name in self.spells[level]:
			print "%s already knows %s." % (self.name, name)
		else:
			self.spells[level].append(name)
			
	def castSpell(self, level):
		self.slots[level] -= 1


def printList(alpha):
	for i in range(len(alpha)):
		print "[%i]: %s" % (i, alpha[i])


if len(argv) > 1:
	fName = argv[1]
else:
	fName = 'party.mgc'
file = open(fName, 'r+')
nCasters = int(file.readline())
casters = ['' for i in range(nCasters)]
names = ['' for i in range(nCasters)]
for i in range(nCasters):
	name = file.readline().rstrip()
	levels = int(file.readline())
	names[i] = name
	casters[i] = Caster(name, levels)

	for k in range(levels):
		numSpells = int(file.readline())
		casters[i].spells[k] = ['' for alpha in range(numSpells)]
		for alpha in range(numSpells):
			casters[i].spells[k][alpha] = file.readline().rstrip()
	for k in range(levels):
		casters[i].slots[k] = int(file.readline())


commands = ['add', 'remove', 'print', 'printall', 'cast']
while 1:
	print "Commands: ", commands,
	command = raw_input(": ")
	command = command.lower()
	if command in commands:
		if command == "printall":
			for i in casters:
				i.printCaster()
		else:
			print "Caster :"
			printList(names)
			target = input("   : ")
			if command == "add" or command == "remove":
				print "Level (0-%i): " % (len(casters[target].slots) - 1)
				level = input("   : ")
				if casters[target].slots[0] != 99:
					level -= 1
				naame = raw_input("Spell name: ")
				if command == "add":
					casters[target].addSpell(level, naame)
				else:
					casters[target].removeSpell(level, naame)
			elif command == "print":
				casters[target].printCaster()
	else:
		print "That is not a valid command."