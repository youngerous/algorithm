from sys import stdin

input = stdin.readline

N = int(input())
for i in range(N):
    print(" " * (i) + "*" * (N - i))
