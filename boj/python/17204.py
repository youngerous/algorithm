from sys import stdin

input = stdin.readline

N, K = map(int, input().split())
death = {n: 1 for n in range(N)}
choices = [int(input()) for _ in range(N)]

next_person = choices[0]
cannot = True
for n in range(N):
    death[next_person] -= 1
    next_person = choices[next_person]
    if death[K] == 0:
        print(n + 1)
        cannot = False
        break

if cannot:
    print(-1)
