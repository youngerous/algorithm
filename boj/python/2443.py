from sys import stdin

input = stdin.readline

N = int(input())
for i in range(N, 0, -1):
    print(" " * (N - i) + "*" * (2 * i - 1))
