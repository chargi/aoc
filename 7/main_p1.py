#Globals
FILENAME = "7/input1.txt"
lines = open(FILENAME, "r").read().splitlines()
root: dict = dict()
underLimit = list()
LIMIT = 100000


print("--- Day 7: No Space Left On Device ---")
print("Part 1 - Find all of the directories with a total size of at most 100000.")
print("What is the sum of the total sizes of those directories?")

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
def getDirSizeAndWriteToGlobals(dir: dict):
    dirsize = int()
    for v in dir.values():
        if (type(v) == type(str())):
            dirsize += int(v)
        if (type(v) == type(dict())):
            subdirsize = getDirSizeAndWriteToGlobals(v)
            if subdirsize <= LIMIT:
                underLimit.append(subdirsize)
            dirsize += subdirsize        
    return dirsize
        

cmdParser(lines)
getDirSizeAndWriteToGlobals(root)
print("Sum of total size of dirs under 100k: {}".format(sum(underLimit)))