#!/usr/bin/env python
#Written 3/22/17, based on probability.py, both by Sam Kleber
total = 0;
print "This program will let you know either the probability that a number of dice will be greater than or equal\nto a value, or the average damage that that combination will deal."
print
print
hitNumber = int(raw_input("How may dice are you rolling to hit: "))
damNumber = int(raw_input("How may dice are you rolling for damage: "))
size = 6
defense = int(raw_input("DEF: "))
arm = int(raw_input("ARM: "))
att = int(raw_input("MAT/RAT: "))
power = int(raw_input("POW: "))
passfail = raw_input("1 HP target? ").lower()
attacks = float(raw_input("Number of attacks: "))
i = 0
possibilities = size ** hitNumber

def sumPoss(number, size, mod, passfail, this_total):
    total = 0
    for i in range(1,size+1):
        if number > 1:
            total += sumPoss(number-1, size, mod, passfail, this_total+i)
        else:
            dummy = this_total + i - mod
            if dummy > 0 and passfail == 'no':
                total += dummy
            elif dummy >= 0 and passfail == 'yes':
                total += 1
    return total

hits = float(sumPoss(hitNumber, size, defense - att, "yes", 0))
if int(hits) == possibilities:
    hits -= 1
hits *= attacks / possibilities
mod = arm - power
if passfail == "yes":
    mod += 1

possibilities = size ** damNumber
wounds = float(sumPoss(damNumber, size, mod, passfail, 0)) * hits / possibilities
print str(hits) + " hits resulting in an average of " + str(wounds),
if passfail == "yes":
    print "kills."
else:
    print "damage."