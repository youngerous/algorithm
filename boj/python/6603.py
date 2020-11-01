from sys import stdin
from itertools import combinations

input = stdin.readline

while True:
    testcase = input().split()
    if testcase[0] == "0":
        break
    else:
        del testcase[0]

    for case in combinations(testcase, 6):
        print(" ".join(case))
    print()
