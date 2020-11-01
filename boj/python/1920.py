from sys import stdin

input = stdin.readline

N = int(input())
nlist = list(map(int, input().split()))
ndict = {n: 1 for n in nlist}

M = int(input())
mlist = list(map(int, input().split()))

ans = [0 if ndict.get(i, 0) == 0 else 1 for i in mlist]
print(*ans, sep="\n")
