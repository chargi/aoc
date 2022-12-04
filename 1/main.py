from operator import itemgetter, attrgetter
from elve import Elve

#Globals
FILENAME = "1/example.txt"

print("Running Elves Calories Calculator")

all_elves = [] #stores all elves created
top_three = [] #top three elves

calories_list = open(FILENAME, "r").read().splitlines()

#Read lines and create Elves with their calories given

arr = [] #temp array for elve creation
for line in calories_list:
    if line.strip():
        arr.append(int(line))
    else:
        if not arr.__len__ == 0:
            all_elves.append(Elve(arr))
        arr = []
#We still have to handle the last elf, not a fancy way to do it
if not arr == []:
    all_elves.append(Elve(arr))


#Find highest calorie sum carried by an elve
highscore = 0
for elve in all_elves:
    if elve.sum > highscore:
        highscore = elve.sum

print("Highest calories are: ")
print(highscore)

#Find top three calorie sum carried by elves
all_elves.sort(key=attrgetter("sum"), reverse=True)
top_three = all_elves[:3]
print("Top 3 Elves Calorie Sum:")
print(sum(e.sum for e in top_three))