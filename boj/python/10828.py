from sys import stdin

input = stdin.readline

N = int(input())
stack = []
for _ in range(N):
    command = input().split()
    if command[0] == "push":
        stack.append(command[1])
    elif command[0] == "pop":
        try:
            print(stack.pop())
        except:
            print(-1)
    elif command[0] == "size":
        print(len(stack))
    elif command[0] == "empty":
        print(1) if len(stack) == 0 else print(0)
    elif command[0] == "top":
        try:
            print(stack[-1])
        except:
            print(-1)
