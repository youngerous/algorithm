from sys import stdin

input = stdin.readline

input()
print(" ".join(map(str, sorted(list(set(map(int, input().split())))))))
