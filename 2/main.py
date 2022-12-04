from figures import *
from playtheory import *

#Globals
FILENAME = "2/example.txt"
winvalue = 6
drawvalue = 3

print("Starting RPS Strategy Calculator")

#Read file and create a list
strategy = open(FILENAME, "r").read().splitlines()

score = 0
for line in strategy:
    arr = line.split(" ")
    score = score+outcome(normalizeFigures(arr[0]),normalizeFigures(arr[1]))

#Output
print("Case 1 - Player score:")
print(score)

#Reset score and go again with strategy approach
score = 0
for line in strategy:
    arr = line.split(" ")
    score = score+strategyResult(normalizeFigures(arr[0]),normalizeFigures(arr[1]))

#Output
print("Case 2 - Player score:")
print(score)
