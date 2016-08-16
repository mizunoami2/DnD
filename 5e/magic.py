#!/usr/bin/env python
from sys import argv

if len(argv) > 1:
	fName = argv[1]
else:
	fName = 'party.mgc'
file = open(fName, 'r+')
nCasters = int(file.readline())
print nCasters