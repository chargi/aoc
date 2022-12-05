from main import *

#Scores
#Lowercase item types a through z have priorities 1 through 26.
#Uppercase item types A through Z have priorities 27 through 52.
assert scoring("y") == 25
assert scoring("e") == 5
assert scoring("A") == 27
assert scoring("Z") == 52
assert scoring("p") == 16
assert scoring("L") == 38
assert scoring("P") == 42
assert scoring("v") == 22
assert scoring("t") == 20
assert scoring("s") == 19