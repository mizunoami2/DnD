#!/usr/bin/env python
import json

data = json.load(open("party.json"))

fFirstSpells = data["Casters"][0]["Spells"][1]
print fFirstSpells[0]