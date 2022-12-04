#Define Figures
class Rock:
    def __init__(self):
        self.name = "Rock"
        self.value = 1
        self.strategy = "Lose"

class Scissors:
    def __init__(self):
        self.name = "Scissors"
        self.value = 3
        self.strategy = "Win"

class Paper:
    def __init__(self):
        self.name = "Paper"
        self.value = 2
        self.strategy = "Draw"

#Normalize Letters to Figures
def normalizeFigures(input):
    if input == "A" or input == "X":
        return Rock()
    if input == "B" or input == "Y":
        return Paper()
    if input == "C" or input == "Z":
        return Scissors()