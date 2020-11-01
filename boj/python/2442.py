from sys import stdin

input = stdin.readline

N = int(input())
for i in range(1, N + 1):
    num_stars = 2 * i - 1
    center = "*" * num_stars
    side = " " * int((2 * N - 1 - num_stars) // 2)
    print(side + center)
