"""
Two-Pointer Algorithm
"""
from sys import stdin

input = stdin.readline

N, M = list(map(int, input().split()))
nlist = list(map(int, input().split()))
count = 0
left, right = 0, 0
current = 0

while True:
    if current >= M:
        current -= nlist[left]
        left += 1
    else:
        if right == N:
            break
        current += nlist[right]
        right += 1
    if current == M:
        count += 1

print(count)
