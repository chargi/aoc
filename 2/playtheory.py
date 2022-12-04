#Define outcome
def outcome(p2figure, p1figure):
    #Draw
    if p1figure.name == p2figure.name:
        return p1figure.value + drawvalue
    #Wins
    if p1figure.name == "Rock" and p2figure.name == "Scissors":
        return p1figure.value + winvalue
    if p1figure.name == "Scissors" and p2figure.name == "Paper":
        return p1figure.value + winvalue
    if p1figure.name == "Paper" and p2figure.name == "Rock":
        return p1figure.value + winvalue
    #Losses
    if p1figure.name == "Scissors" and p2figure.name == "Rock":
        return p1figure.value
    if p1figure.name == "Paper" and p2figure.name == "Scissors":
        return p1figure.value
    if p1figure.name == "Rock" and p2figure.name == "Paper":
        return p1figure.value

def createWinnerFigure(figure):
    if figure.name == "Rock":
        return Paper()
    if figure.name == "Paper":
        return Scissors()
    if figure.name == "Scissors":
        return Rock()

def createDrawFigure(figure):
    if figure.name == "Rock":
        return Rock()
    if figure.name == "Paper":
        return Paper()
    if figure.name == "Scissors":
        return Scissors()

def createLoserFigure(figure):
    if figure.name == "Rock":
        return Scissors()
    if figure.name == "Paper":
        return Rock()
    if figure.name == "Scissors":
        return Paper()

def strategyResult(left, right):
    if right.strategy == "Win":
        return outcome(left,createWinnerFigure(left))    
    if right.strategy == "Draw":
        return outcome(left,createDrawFigure(left))
    if right.strategy == "Lose":
        return outcome(left,createLoserFigure(left))