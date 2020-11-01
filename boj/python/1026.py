from sys import stdin

input = stdin.readline

N = int(input())  # <= 50
A = list(map(int, input().split()))  # 0~100
B = list(map(int, input().split()))  # 0~100

A.sort()
ans = 0
for a in A:
    ans += a * max(B)
    B[B.index(max(B))] = -1
print(ans)
