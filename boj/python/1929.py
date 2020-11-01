from sys import stdin

input = stdin.readline

M, N = map(int, input().split())
is_prime = [False, False] + [True] * (N - 1)
primes = []

# 에라토스테네스의 체
for i in range(2, N + 1):
    if is_prime[i]:
        if i >= M:
            primes.append(i)
        for j in range(2 * i, N + 1, i):
            is_prime[j] = False

for k in primes:
    print(k)
