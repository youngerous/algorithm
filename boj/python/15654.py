from itertools import permutations
from sys import stdin

input = stdin.readline

M = int(input().split()[1])
arr = sorted(list(map(int, input().split())))
arr = map(str, arr)  # in order to use 'join'

for each in permutations(arr, M):
    print(" ".join(each))
