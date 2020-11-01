from sys import stdin

input = stdin.readline

"""
    시간초과 답안
"""


def z(size, r, c):
    global count
    if size <= 2:
        if r == R and c == C:
            print(count)
            return
        count += 1
        if r == R and c + 1 == C:
            print(count)
            return
        count += 1
        if r + 1 == R and c == C:
            print(count)
            return
        count += 1
        if r + 1 == R and c + 1 == C:
            print(count)
            return
        count += 1
        return
    z(size // 2, r, c)  # 1사분면
    z(size // 2, r, c + size // 2)  # 2사분면
    z(size // 2, r + size // 2, c)  # 3사분면
    z(size // 2, r + size // 2, c + size // 2)  # 4사분면


N, R, C = map(int, input().split())
count = 0
z(2 ** N, 0, 0)
