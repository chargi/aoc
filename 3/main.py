#Globals
FILENAME = "3/example.txt"
rucksack_list = open(FILENAME, "r").read().splitlines()
items = {}

#Lowercase item types a through z have priorities 1 through 26.
#Uppercase item types A through Z have priorities 27 through 52.
def scoring(char):
    #ascii A=65, Z=90 - a=97, z=122
    value = ord(char)
    #a-z
    if value >= 97 and value <= 122:
        return(value-96)
    #A-Z
    if value >= 65 and value <= 90:
        return(value-38)

#Read lines and put half of items in each compartment
def part1(rucksack):
    score = 0

    for line in rucksack:
        half_length = len(line)//2
        left = line[:half_length]
        right = line[half_length:]
        #Find first item that is also found in the other compartment, cancel search and add priority score
        found = False
        for l in left:
            if found:
                break
            for r in right:
                if l == r:
                    found = True
                    score += scoring(l)
                    break
    return score

#not beautiful but gets the job done
def part2(rucksack):
    
    score = 0
    
    while rucksack:
        group = []
        found = False

        i = 0
        while i <= 2:
            if rucksack:
                group.append(rucksack.pop())
                i=i+1

        if not group:
            break

        for c1 in group[0]:
            if found:
                break
            for c2 in group[1]:
                if found:
                    break
                if c1==c2:
                    for c3 in group[2]:
                        if c1==c3:
                            score += scoring(c1)
                            found = True
                            break
    return score
    


#Output priority score
print("P1 - Sum of item priorities:")
print(part1(rucksack_list))
print("P2 - Sum of badge priorities:")
print(part2(rucksack_list))