#Globals
FILENAME = "3/example.txt"
rucksack_list = open(FILENAME, "r").read().splitlines()
items = {}

#Lowercase item types a through z have priorities 1 through 26.
#Uppercase item types A through Z have priorities 27 through 52.
def scoring(char):
    #ascii A=65, Z=90 - a=97, z=122
    value = ord(char)
    if char.islower():
        return(value-96)
    else:
        return(value-38)

#Read lines and put half of items in each compartment
def part1(rucksack):
    score = 0
    for line in rucksack:
        half_length = len(line)//2
        left = line[:half_length]
        right = line[half_length:]
        #Find first item that is also found in the other compartment, cancel search and add priority score
        for l in left:
            if l in right:
                score += scoring(l)
                break
    return score

#find the one exact item (character) that is common between the three elves and add up priority of the item
def part2(rucksack):
    score = 0
    for i in range(0, len(rucksack), 3):
        line1 = rucksack[i]
        line2 = rucksack[i+1]
        line3 = rucksack[i+2]
        for c in line1:
            if c in line2 and c in line3:
                score += scoring(c)
                break
    return score
    


#Output priority score
print("P1 - Sum of item priorities:")
print(part1(rucksack_list))
print("P2 - Sum of badge priorities:")
print(part2(rucksack_list))