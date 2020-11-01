from sys import stdin

input = stdin.readline

N = int(input())
deque = []

for _ in range(N):
    command = input().split()
    if command[0] == "push_front":
        deque.insert(0, command[1])
    elif command[0] == "push_back":
        deque.append(command[1])
    elif command[0] == "pop_front":
        print(deque.pop(0)) if deque else print(-1)
    elif command[0] == "pop_back":
        print(deque.pop()) if deque else print(-1)
    elif command[0] == "size":
        print(len(deque))
    elif command[0] == "empty":
        print(1 - int(bool(deque)))
    elif command[0] == "front":
        print(deque[0]) if deque else print(-1)
    elif command[0] == "back":
        print(deque[-1]) if deque else print(-1)
