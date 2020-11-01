from sys import stdin

input = stdin.readline

N = int(input())
for _ in range(N):
    ps = input().strip()
    if ps.count("(") != ps.count(")"):
        print("NO")
        continue
    # 처음부터 stack을 int 0으로 할당하면 시간을 더 줄일 수 있을 것
    stack = []
    try:
        for each in ps:
            stack.append(each) if each == "(" else stack.pop()
    except Exception as e:
        print("NO")
        continue
    print("YES") if len(stack) == 0 else print("NO")
