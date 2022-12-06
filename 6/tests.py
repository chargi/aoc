from main import *

assert markChecker("mjqjpqmgbljsphdztnvjfqwrcgsmlb",4) == 7
assert markChecker("bvwbjplbgvbhsrlpgdmjqwftvncz",4) == 5
assert markChecker("nppdvjthqldpwncqszvftbrmjlhg",4) == 6
assert markChecker("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",4) == 10
assert markChecker("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw",4) == 11

assert markChecker("mjqjpqmgbljsphdztnvjfqwrcgsmlb",14) == 19
assert markChecker("bvwbjplbgvbhsrlpgdmjqwftvncz",14) == 23
assert markChecker("nppdvjthqldpwncqszvftbrmjlhg",14) == 23
assert markChecker("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",14) == 29
assert markChecker("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw",14) == 26