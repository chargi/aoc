from figures import *
from playtheory import *

#Globals
FILENAME = "2/example.txt"
strategy = open(FILENAME, "r").read().splitlines()

print("Starting RPS Strategy Calculator")

score = 0
for line in strategy:
    arr = line.split(" ")
    score += outcome(normalizeFigures(arr[0]),normalizeFigures(arr[1]))

#Output
print("Case 1 - Player score:")
print(score)

#Reset score and go again with strategy approach
score = 0
for line in strategy:
    arr = line.split(" ")
    score += strategyResult(normalizeFigures(arr[0]),normalizeFigures(arr[1]))

#Output
print("Case 2 - Player score:")
print(score)
