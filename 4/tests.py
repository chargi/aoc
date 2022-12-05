from main import *

assert checkPartialOverlap(1,2,3,4) == False
assert checkPartialOverlap(1,2,2,4) == True
assert checkPartialOverlap(2,2,2,4) == True
assert checkPartialOverlap(1,3,4,4) == False
assert checkPartialOverlap(1,1,2,2) == False
assert checkPartialOverlap(1,5,1,5) == True
assert checkPartialOverlap(1,1,1,1) == True
assert checkPartialOverlap(10,11,10,12) == True
assert checkPartialOverlap(10,11,12,13) == False
assert checkPartialOverlap(10,11,9,10) == True
assert checkPartialOverlap(10,11,10,10) == True
assert checkPartialOverlap(10,15,15,15) == True
assert checkPartialOverlap(100,115,200,4000) == False
assert checkPartialOverlap(10,15,1,15) == True
assert checkPartialOverlap(10,15,1,10) == True
assert checkPartialOverlap(10,15,1,9) == False
assert checkPartialOverlap(3,10,4,14) == True
assert checkPartialOverlap(14,16,1,15) == True

assert checkPartialOverlap(2,4,6,8) == False
assert checkPartialOverlap(2,3,4,5) == False
assert checkPartialOverlap(5,7,7,9) == True
assert checkPartialOverlap(2,8,3,7) == True
assert checkPartialOverlap(6,6,4,6) == True
assert checkPartialOverlap(2,6,4,8) == True