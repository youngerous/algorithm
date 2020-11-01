from sys import stdin

input = stdin.readline

N = int(input())
M = input().strip()

total = 0
for (i, each) in enumerate(reversed(M)):
    part = N * int(each)
    print(part)
    total += part * (10 ** (i))
print(total)
