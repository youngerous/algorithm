from sys import stdin

input = stdin.readline

N = int(input())
for i in range(1, 2 * N):
    i = 2 * N - i if i > N else i
    stars = "*" * (2 * i - 1)
    space = " " * (((2 * N - 1) - len(stars)) // 2)
    print(space + stars)
