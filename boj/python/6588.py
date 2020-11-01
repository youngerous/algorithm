from sys import stdin

input = stdin.readline


def get_primes(num):
    smaller_primes = []
    for n in range(2, num + 1):
        if (is_prime[n]) and (n % 2 != 0):
            smaller_primes.append(n)
        for k in range(2 * n, num + 1, n):
            is_prime[k] = False
    return smaller_primes


def check_hypothesis(num, prime_nums):
    for p in prime_nums:
        if is_prime[num - p]:
            print("{} = {} + {}".format(num, p, num - p))
            return
    print("Goldbach's conjecture is wrong")


MAX_NUM = 1000000
is_prime = [False, False] + [True] * (MAX_NUM - 1)
primes = get_primes(MAX_NUM)  # 1,000,000보다 작은 소수 모두 구하기
while True:
    N = int(input())
    if N == 0:
        break
    check_hypothesis(N, primes)  # 소수들의 조합으로 N이 만들어지는지 확인
