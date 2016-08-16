#!/usr/bin/env python
from sys import argv

if argv.size > 1:
	fName = argv[1]
else:
	fName = 'party.mgc'
file = open(fName, 'r+')
nCasters = int(file.readline())
print nCasters