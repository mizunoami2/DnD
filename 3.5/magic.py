#!/usr/bin/env python
from sys import argv
import json

def printList(alpha):
	for i in range(len(alpha)):
		print "[%i]: %s" % (i, alpha[i])

class Caster(object):
	def __init__(self, name, levels, meth):
		self.name = name
		self.spells = ['' for i in range(levels)]
		self.slots = ['' for i in range(levels)]
		self.meth = meth

#	def printCaster(self):
#NEEDED for 3.5	

	def removeSpell(self, level, name):
		if name in self.spells[level]:
			self.spells[level].remove(name)
		else:
			print "%s doesn't know %s." % (self.name, name)

	def addSpell(self, level, name):
		if name in self.spells[level] and self.meth == "Sorc":
			print "%s already knows %s." % (self.name, name)
		else:
			self.spells[level].append(name)

	def addSlot(self, level):
		if self.meth == "Prep":
			print "%s doesn't have spell slots." % (self.name)
		else:
			self.slots[level] += 1

	def removeSlot(self, level):
		if self.meth == "Prep":
			print "%s doesn't have spell slots." % (self.name)
		else:
			if self.slots[level] == 0:
				print "%s has no more level %i slots left." % (self.name, level)
			else:
				self.slots[level] -= 1

	def printCaster(self):
		print self.name
		if self.meth == "Spon":
			for i in range(len(self.spells)):
				print "\nLevel %i Spells (%i slots left): " %(i, self.slots[i])
				printList(self.spells[i])
		elif self.meth == "Prep":
			for i in range(len(self.spells)):
				print "\nLevel %i Spells: " %(i)
				printList(self.spells[i])
		print
		print



fName="party.json"
if len(argv) > 1:
	fName = argv[1]
data = json.load(open(fName))
casters = ['' for i in data]
names = ['' for i in data]
for i in range(len(data)):
	dummy = data[i]
	casters[i] = Caster(dummy["Name"], len(dummy["Spells"]), dummy["Meth"])
	names[i]= dummy['Name']
	casters[i].spells = dummy["Spells"]
	if dummy["Meth"] == "Spon":
		casters[i].slots = dummy["Slots"]


commands = ['add', 'addslot', 'remove', 'removeslot', 'print', 'printall', 'cast', 'quit']
while 1:
	print "********** Commands: ", commands,
	command = raw_input(": ")
	command = command.lower()
	if command in commands:
		print "*" * 10, command.upper(), "*" * 10
		if command == "printall":
			for i in casters:
				i.printCaster()
		elif command == "quit":
			oname = str(input("Name of file to write: "))
			outf = open(oname, 'w+')
			outf.write("[\n")
			for i in range(len(casters)):
				outdict = casters[i].__dict__
				outdict = dict((k.capitalize(), v) for k,v in outdict.iteritems())
				outf.write(json.dumps(outdict, indent=4))
				if i + 1 < len(casters):
					outf.write(",")
			outf.write("]")
			exit(0)
		else:
			print "Caster: "
			printList(names)
			target = input("   : ")
			print
			if command[0:3] == "add" or command[0:6] == "remove":
				level = input("Level (0-%i): " % (len(casters[target].slots) - 1))
				if command[-4:] == "slot":
					if command == "addslot":
						casters[target].addSlot(level)
					else:
						casters[target].removeSlot(level)
				else:
					name = raw_input("Spell name: ")
					if command == "add":
						casters[target].addSpell(level, name)
					else:
						casters[target].removeSpell(level, name)
			elif command == "print":
				casters[target].printCaster()
			elif command == "cast":
				level = input("Level (0-%i): " % (len(casters[target].slots) - 1))
				if casters[target].slots[level] == 99:
					print "That wasn't necessary, cantrips can be cast infinitely."
				elif casters[target].slots[level] == 0:
					print "%s is out of level %i slots." % (casters[target].name, level)
				else:
					casters[target].slots[level] -= 1
	else:
		print "That is not a valid command."