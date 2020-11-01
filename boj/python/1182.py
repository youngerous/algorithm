from itertools import combinations
from sys import stdin

input = stdin.readline

S = list(map(int, input().split()))[1]
nlist = list(map(int, input().split()))
count = 0

for sublist in range(1, len(nlist) + 1):
    for elm in combinations(nlist, sublist):
        if sum(elm) == S:
            count += 1

print(count)
