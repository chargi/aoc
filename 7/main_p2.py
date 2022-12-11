#Globals
FILENAME = "7/example.txt"
lines = open(FILENAME, "r").read().splitlines()
root: dict = dict()
overLimit = list()
TOTAL = 70000000
TARGET = 30000000


print("--- Day 7: No Space Left On Device ---")
print("Part 2 - Find the smallest directory that, if deleted, would free up enough space on the filesystem to run the update.")
print("What is the total size of that directory?")

def getCmdTokens(cmd):
    return cmd.split(" ")

def cmdParser(commands):
    cd: dict = root  #current directory
    prev: list = list() #pop last level from there
    for line in commands:
        cmd_tokens = getCmdTokens(line)
        if line.startswith("$ cd /"):
            cd = root
            # print("Setting current directory to root")
        if line.startswith("$ ls"):
            # print("Listing current directory")
            pass
        if line.startswith("dir"):
            cd.setdefault(cmd_tokens[1],dict())  #key = dirname, value = new dict
            # print("Creating directory {}".format(cmd_tokens[1]))
        if len(cmd_tokens) == 2 and cmd_tokens[0].isnumeric():
            cd.setdefault(cmd_tokens[1], cmd_tokens[0])  #key = filename, value = filesize
            # print("Creating file {}".format(cmd_tokens[1]))
        if line == "$ cd ..":
            cd = prev.pop()
            # print("Going up a directory level")
        if line.startswith("$ cd ") and len(cmd_tokens) == 3 and not cmd_tokens[2] == "/" and not cmd_tokens[2] == "..":
            prev.append(cd)
            cd = cd.get(cmd_tokens[2])
            # print("Setting current directory to {}".format(cmd_tokens[2]))
    return root

# Files can be counted multiple times with this algorithm, which is explained in the requirement
def getDirSizeAndWriteToGlobals(dir: dict, limit: int):
    dirsize = int()
    for v in dir.values():
        if (type(v) == type(str())):
            dirsize += int(v)
        if (type(v) == type(dict())):
            subdirsize = getDirSizeAndWriteToGlobals(v,limit)
            if subdirsize >= limit:
                overLimit.append(subdirsize)
            dirsize += subdirsize        
    return dirsize
        

cmdParser(lines)
usedSpace = getDirSizeAndWriteToGlobals(root,0)
print("Space used: {}".format(usedSpace))

freeSpace = TOTAL-usedSpace
neededSpace = TARGET-freeSpace

overLimit.clear()
getDirSizeAndWriteToGlobals(root,neededSpace)
overLimit.sort()
print(max(overLimit))