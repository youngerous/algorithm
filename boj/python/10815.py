from sys import stdin

input = stdin.readline

input()
ndict = dict((item, 1) for item in list(map(int, input().split())))
input()
mlist = list(map(int, input().split()))

for m in mlist:
    print(0) if ndict.get(m, 0) == 0 else print(1)
