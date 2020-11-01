from sys import stdin

input = stdin.readline

N = int(input())
nlist = list(map(int, input().split()))
M = int(input())
mlist = list(map(int, input().split()))

ndict = {}
for n in nlist:
    ndict[n] = ndict.get(n, 0) + 1
for m in mlist:
    print(ndict.get(m, 0), end=" ")
