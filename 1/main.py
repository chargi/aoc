from operator import attrgetter
from elve import Elve

#Globals
FILENAME = "1/example.txt"
all_elves = [] #stores all elves created
top_three = [] #top three elves
calories_list = open(FILENAME, "r").read().splitlines()

print("Running Elves Calories Calculator")

temp_calories = [] #temp list of calories for elve creation
for line in calories_list:
    if line.strip():
        temp_calories.append(int(line))
    else:
        if temp_calories:
            all_elves.append(Elve(temp_calories))
        temp_calories = []
#We still have to handle the last elf, not a fancy way to do it but at least it doesn't break
if temp_calories:
    all_elves.append(Elve(temp_calories))

all_elves.sort(key=attrgetter("sum"), reverse=True)

#Find highest calorie sum carried by an elve
print("Highest calories are: ")
print(all_elves[0].sum)

#Find top three calorie sum carried by elves
top_three = all_elves[:3]
print("Top 3 Elves Calorie Sum:")
print(sum(e.sum for e in top_three))