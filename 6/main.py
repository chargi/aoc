#Globals
FILENAME = "6/example.txt"
lines = open(FILENAME, "r").read().splitlines()
line = lines[0]
print("## Day 6 - Tuning Trouble ##")
print("Find the markers in a given string")

def markChecker(toCheck, uniqueCount):
    start = 0
    for c in toCheck:
        temp = toCheck[start:start+uniqueCount]
        check = set(temp)
        if len(check) == uniqueCount:
            return start+uniqueCount
        check.clear()
        start += 1
    return -1

#print(markChecker(line, 4))
#print(markChecker(line, 14))