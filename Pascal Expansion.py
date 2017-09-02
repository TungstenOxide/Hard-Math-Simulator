#!/usr/bin/env Python
import operator as op
import sys

def ncr(n, r):
    r = min(r, n-r)
    if r == 0: return 1
    numer = reduce(op.mul, xrange(n, n-r, -1))
    denom = reduce(op.mul, xrange(1, r+1))
    return numer//denom

def printExpand():
    for x in range (0, exponent+1):
        sys.stdout.write(output[x] + " ")
        sys.stdout.flush()
    print

print("Pascal Expansion")
problem = raw_input("Enter binomial term > ")
exp = 0
while not problem[exp] == ")":
    exp += 1
exp += 2
wheres = len(problem) - exp
exponent = int(problem[-wheres:])
output = []
#Pascal Triangle Row
for x in range (0, exponent+1):
    output.append(str(ncr(exponent, x)))
    # print output[x]
# print("Get the Pascal Triangle Row (Row " + str(exponent) + ")")
# printExpand()
#/Pascal Triangle Row
#First Term
get = 1
termOne = ""
isNegative = False
while not problem[get] == str("+"):
    if problem[get] == str("-"):
        # print ("Found a negative")
        if (get > 1):
            # print ("Negative is past the one position")
            isNegative = True
            break
    termOne += (problem[get])
    get += 1
termOne = "(" + termOne + ")"
# print("Input the first term")
for x in range (0, exponent):
    output[x] = (output[x] + termOne)
# printExpand()
#/First Term
#First exponent
expOne = exponent
# print("Add the first exponent")
for x in range (0, exponent):
    output[x] = (output[x] + "^" + str(expOne) + " ")
    expOne -= 1
# printExpand()
#/First exponent
#Second Term
get += 1
termTwo = ""
while not problem[get] == str(")"):
    termTwo += (problem[get])
    get += 1
if isNegative == True:
    termTwo = "(-" + termTwo + ")"
else:
    termTwo = "(" + termTwo + ")"
# print("Input the second term")

for x in range (1, exponent+1):
    output[x] = (output[x] + termTwo)
# printExpand()
#/Second Term
#Second exponent
expTwo = 1
# print("Add the second exponent")
for x in range (1, exponent+1):
    output[x] = (output[x] + "^" + str(expTwo))
    expTwo += 1
# printExpand()
#/Second exponent
#Add pluses
# print("And finally...")
print
for x in range (0, exponent):
    output[x] = (output[x] + " +")
printExpand()
#/Pluses
print("\nExpanded...")
#Solving!!!
# for x in range (0, exponent+1):

#/Solving


#Use this to edit the list items later
# for x in range (0, exponent+1):
#     output[x] = (output[x] + "MEMES!?")
#     print output[x]
