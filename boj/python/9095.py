import itertools
from sys import stdin

input = stdin.readline

# Brute Force로 풀었기 때문에 정답이지만 시간이 매우 오래 걸린다.
input()
for n in list(map(int, stdin.read().split())):
    count = 0
    for one in range(n // 1 + 1):
        for two in range(n // 2 + 1):
            for three in range(n // 3 + 1):
                if one * 1 + two * 2 + three * 3 == n:
                    combination = [1] * one + [2] * two + [3] * three
                    count += len(set(c for c in itertools.permutations(combination)))
    print(count)
