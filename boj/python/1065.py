from sys import stdin

input = stdin.readline
N = int(input())

total = 0
for num in range(1, N + 1):
    if num < 100:
        total += 1
        continue
    n_list = list(map(int, str(num)))
    if n_list[0] - n_list[1] == n_list[1] - n_list[2]:
        total += 1
print(total)
