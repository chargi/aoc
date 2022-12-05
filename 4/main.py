#Globals
FILENAME = "4/example.txt"
score = 0
score2 = 0

def checkOverlap(origin_left, origin_right, target_left, target_right):
    if origin_left <= target_left and origin_right >= target_right:
        return True
    if target_left <= origin_left and target_right >= origin_right:
        return True
    return False

def checkPartialOverlap(origin_left, origin_right, target_left, target_right):
    if checkOverlap(origin_left, origin_right,target_left, target_right):
        return True
    if origin_left >= target_left and origin_left <= target_right:
        return True
    if target_left >= origin_left and target_left <= origin_left:
        return True
    if origin_right >= target_left and origin_right <= target_right:
        return True
    if target_right >= origin_left and target_right <= origin_left:
        return True    
    return False

lines = open(FILENAME, "r").read().splitlines()

for line in lines:
    camps = line.split(",")
    camps_left = camps[0].split("-")
    camps_right = camps[1].split("-")

    if checkOverlap(int(camps_left[0]), int(camps_left[1]), int(camps_right[0]), int(camps_right[1])):
        score += 1
    if checkPartialOverlap(int(camps_left[0]), int(camps_left[1]), int(camps_right[0]), int(camps_right[1])):
        score2+= 1

#Print overlapped plans
print("P1 - Overlaps: ")
print(score)
print("P2 - Partial Overlaps: ")
print(score2)