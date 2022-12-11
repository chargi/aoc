import math

#Globals
FILENAME = "8/example.txt"
lines = open(FILENAME, "r").read().splitlines()
print("--- Day 8: Treetop Tree House ---")
print("How many trees are visible from outside the grid?")

# Read 2d array and convert to int in the process
rect = list()
for line in lines:
    temp = list()
    for c in line:
        temp.append(int(c))
    rect.append(temp)

def getPartialScenicScore(treesAligned: list, value: int):
    counter = 0
    for x in treesAligned:
        counter += 1
        if x >= value:
            break
    return counter

def findVisibleTrees(grid):
    def selectColValues(start,end,col):
        result = list()
        for x in range(start,end):
            result.append(grid[x][col])
        return result

    # Find border trees (all visible):
    treesCount = len(grid[0])*2+(len(grid)-2)*2
    print("Border trees found: {}".format(treesCount))

    xMaxIndex = len(grid)-1
    yMaxIndex = len(grid[0])-1
    xSize = len(grid)
    ySize = len(grid[0])
    x = 0
    y = 0
    scenicHighscore = 0
    for x in range(1,xMaxIndex):
        for y in range(1,yMaxIndex):
            oVal = grid[x][y]
            checkLeft = grid[x][0:y]
            checkRight = grid[x][y+1:ySize]
            checkTop = selectColValues(0,x,y)
            checkBottom = selectColValues(x+1,xSize,y)

            # Check if tree is visible from the outside
            if all(oVal > x for x in checkLeft) or all(oVal > x for x in checkRight) or all(oVal > x for x in checkTop) or all(oVal > x for x in checkBottom):
                treesCount += 1
            
            # Calculate tree's scenic score and update highscore
            scenicMultipliers = [getPartialScenicScore(reversed(checkLeft),oVal),getPartialScenicScore(checkRight,oVal),getPartialScenicScore(reversed(checkTop),oVal),getPartialScenicScore(checkBottom,oVal)]

            scenicScore = math.prod(scenicMultipliers)
            if scenicScore > scenicHighscore:
                scenicHighscore = scenicScore

    print("Highest scenic score: {}".format(scenicHighscore))
    return treesCount

print("Total trees visible: {}".format(findVisibleTrees(rect)))