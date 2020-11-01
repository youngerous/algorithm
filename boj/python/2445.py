from sys import stdin

input = stdin.readline

N = int(input())
for i in range(1, N + 1):
    stars = "*" * (i)
    spaces = " " * (2 * N - 2 * i)
    print(stars + spaces + stars)

for i in range(1, N + 1):
    stars = "*" * ((2 * N - 2 * i) // 2)
    spaces = " " * (2 * N - len(stars) * 2)
    print(stars + spaces + stars)
