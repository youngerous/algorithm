from sys import stdin

input = stdin.readline

N = int(input())
for _ in range(N):
    print("god{}".format("".join(input().split()[1:])))
