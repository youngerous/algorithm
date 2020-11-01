from sys import stdin

input = stdin.readline

N = int(input())
queue = []
for _ in range(N):
    command = input().split()
    if command[0] == "push":
        queue.append(command[1])
    elif command[0] == "pop":
        if queue:
            print(queue[0])
            del queue[0]
        else:
            print(-1)
    elif command[0] == "size":
        print(len(queue))
    elif command[0] == "empty":
        print(1 - int(bool(queue)))
    elif command[0] == "front":
        print(queue[0]) if queue else print(-1)
    elif command[0] == "back":
        print(queue[-1]) if queue else print(-1)
