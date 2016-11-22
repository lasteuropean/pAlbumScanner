# A program that scans a text file anticipating lists in the format of [one or two digit numbers][band name] - [album name]
# and applies a weighted score based on rank, printing a final tally

import re

#dictionaries for 1. @dicAdd,  2. @dicAdd2 3. @dicMerge
dK = {}
dK2 = {}
dK3 = {}

def main():
    scanThisFile('r1.txt')
    dicMerge(dK2, dK)
    printDic1(dK3)

# Scan specified file @param and look for pattern with @function 
#
# @param    *args   filename
# @function re.compile  Looks for 
# 0 or 1 occurrences of numbers in the first and second position
# Any occurrences of characters
# One space and a dash
# Any occurrences of characters

def scanThisFile(*args):
    pattern = re.compile(r'(\A\d{1,2})\W*((\w+\W+)*)\W?-((\W?\w+)*)')

    with open(args[0], encoding = "ISO-8859-1") as f:
        for line in f:
            match = re.search(pattern, line)
            if match:
                dicAdd(match.group(2).lower(),(int(match.group(1))))
                dicAdd2(match.group(2).lower(), match.group(4).lower())


# Build dK; pairing a key with a score that applies higher weight to lower scores
#
# @param    al any string, presumably a band name
# @param    sc number between 1 and 15
# @constant x Maximum used for bounding the equation

def dicAdd(al, sc):
    x = 16
    if al not in dK:
        dK[al] = ((sc * ((sc + x)*(x-sc))/(x * sc)))
    else:
        dK[al] += (sc * (((sc + x)*(x-sc))/(x * sc)))

# Build dK2; pairing a key with the data in the final column
# 
# @param al     any string, presumably a band name
# @param nnn    any string, presumably an album name

def dicAdd2(al, nnn):
    if al not in dK2:
        dK2[al] = nnn

# Build dK3 pairing a new key (the band name + the album name) and the score
# So if the string in the score dictionary matches a value in the reference dictionary
# then create a dictionary that appends those two strings, and attach the associated score
#
# @param dn  dK2: reference dictionary     
# @param ds  dK: score dictionary has final scores

def dicMerge(dn,ds):
    for items in sorted(ds.items()):
        if items[0] in dn:
            dK3[items[0] + str(dn[items[0]])] = items[1]
            
            
# Prints a formatted view of 
# @param    dd dictionary  

def printDic1(dd):        
    for item in sorted(dd.items()):
        print(item[0], ",", item[1])
        
if __name__ == "__main__": main()
