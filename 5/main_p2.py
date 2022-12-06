#Globals
FILENAME = "5/example.txt"
lines = open(FILENAME, "r").read().splitlines()
print("--- Day 5: Supply Stacks ---")
print("Crane Game - Part 1")

commands = []
pillars = []
amount = 0


class Command:
    def __init__(self,input: str) -> None:
        self.data = input.split(" ")
        self.amount = int(self.data[1])
        self.source = int(self.data[3])-1
        self.target = int(self.data[5])-1

#Read data
for line in reversed(lines):
    pillar = 1
    line_str = str(line)
    
    if line_str.startswith("move"):
        commands.append(Command(line_str))

    if line_str.startswith(" 1"):
        pillar_nos = len(line_str.split("   "))
        for i in range(0,pillar_nos,1):
            pillars.append([])

    if line_str.count("[") > 0:
        for i in range(1,len(line_str),4):
            if line_str[i].isalpha():
                pillars[pillar-1].append(line_str[i])
                print("Added {} to pillar {}".format(line_str[i],pillar))
            pillar += 1

#Do the crane thingy
for cmd in reversed(commands):
    crate_buffer = []
    for i in range(0,cmd.amount,1):
        if len(pillars[cmd.source]) > 0:
            crate_buffer.append(pillars[cmd.source].pop())
    for crate in reversed(crate_buffer):
        pillars[cmd.target].append(crate)
    crate_buffer.clear()

#Create result message for riddle
result = ""
for pillar in pillars:
    if len(pillar) > 0:
        result += pillar[len(pillar)-1]
print("Message: {}".format(result))