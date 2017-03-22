#!/usr/bin/env python
#written by Sam Kleber, 3/14/17
total = 0;
print "This program will let you know either the probability that a number of dice will be greater than or equal\nto a value, or the average damage that that combination will deal."
print
print
number = int(raw_input("How may dice are you rolling: "))
size = int(raw_input("How many sides on the dice: "))
mod = int(raw_input("What is the value needed to beat: "))
hits = float(raw_input("Number of attacks/hits: "))
passfail = raw_input("Does it matter how much it beats the value by? ")
passfail = passfail.lower()
i = 0
possibilities = size ** number

def sumPoss(number, size, mod, passfail, this_total):
    total = 0
    for i in range(1,size+1):
        if number > 1:
            total += sumPoss(number-1, size, mod, passfail, this_total+i)
        else:
            dummy = this_total + i - mod
            if dummy > 0 and passfail == 'yes':
                total += dummy
            elif dummy >= 0 and passfail == 'no':
                total += 1
    return total

print float(sumPoss(number, size, mod, passfail, 0)) * hits / possibilities ,
if passfail == 'yes':
    print "expected total damage."
else:
    print "expected total hits."