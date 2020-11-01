from sys import stdin

input = stdin.readline

sizes = list(map(int, input().split()))
N, M = sizes[0], sizes[1]
A, B = list(map(int, input().split())), list(map(int, input().split()))
idx_a, idx_b = 0, 0

ans = []
while (idx_a < N) and (idx_b < M):
    if A[idx_a] > B[idx_b]:
        ans.append(B[idx_b])
        idx_b += 1
    else:
        ans.append(A[idx_a])
        idx_a += 1

while idx_a < N:
    ans.append(A[idx_a])
    idx_a += 1

while idx_b < M:
    ans.append(B[idx_b])
    idx_b += 1

print(" ".join(map(str, ans)))
