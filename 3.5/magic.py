#!/usr/bin/env python
from sys import argv
import json

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

	def castSpell(self, level):
		self.slots[level] -= 1

def printList(alpha):
	for i in range(len(alpha)):
		print "[%i]: %s" % (i, alpha[i])




fName="party.json"
if len(argv) > 1:
	fName = argv[1]
data = json.load(open(fName))
casters = ['' for i in data["Casters"]]
for i in range(len(data["Casters"])):
	dummy = data["Casters"][i]
	casters[i] = Caster(dummy["Name"], len(dummy["Spells"]), dummy["Meth"])
print json.dumps(casters[0].__dict__, indent=4)
outdict = casters[0].__dict__
outdict = {k.capitalize():v
    for k, v in
    outdict.iteritems()
}
print json.dumps(outdict, indent=4)

print outdict["Name"]
commands = ['add', 'remove', 'print', 'printall', 'cast', 'quit']
while 1:
	print "********** Commands: ", commands,
	command = raw_input(": ")
	command = command.lower()
	if command in commands:
		if command == "printall":
			for i in casters:
				i.printCaster()
		elif command == "quit":
			oname = input("Name of file to write: ")
			outf = open(oname, 'w')
			wl(outf, len(casters))
			for cas in casters:
				wl(outf, cas.name)
				wl(outf, len(cas.spells))
				for spl in cas.spells:
					wl(outf, len(spl))
					for spell in spl:
						wl(outf, spell)
				for slot in cas.slots:
					wl(outf, slot)
			exit(0)
		else:
			print "Caster :"
			printList(names)
			target = input("   : ")
			if command == "add" or command == "remove":
				level = input("Level (0-%i): " % (len(casters[target].slots) - 1))
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