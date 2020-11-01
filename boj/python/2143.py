from itertools import combinations
from sys import stdin

input = stdin.readline

T = int(input())
N, alist = int(input()), list(map(int, input().split()))
M, blist = int(input()), list(map(int, input().split()))

dict_A = {}
for idx in range(N):
    current = 0
    for jdx in range(idx, N):
        current += alist[jdx]
        # if current < T:
        dict_A[current] = (
            dict_A[current] + 1 if (dict_A.get(current)) and (current < T) else 1
        )

dict_B = {}
for idx in range(M):
    current = 0
    for jdx in range(idx, M):
        current += blist[jdx]
        # if current < T:
        dict_B[current] = (
            dict_B[current] + 1 if (dict_B.get(current)) and (current < T) else 1
        )


# print(dict_A)
# print(dict_B)
count = 0
for aa in dict_A:
    if dict_B.get(T - aa):
        count += dict_A[aa] * dict_B[T - aa]
# for elm_a in list(dict_A.keys()):
#     for elm_b in list(dict_B.keys()):
#         if elm_a + elm_b == T:
#             count += (dict_A[elm_a]*dict_B[elm_b])
print(count)
