def operation(otype, b, a):
    if otype == "+":
        return a + b
    elif otype == "-":
        return a - b
    elif otype == "*":
        return a * b
    elif otype == "/":
        return a // b  # must be integer


T = int(input())
for test_case in range(1, T + 1):
    forth = list(input().split())
    types = ["+", "-", "/", "*", "."]
    stack = []

    for idx, elm in enumerate(forth):
        if elm not in types:
            stack.append(int(elm))
            continue

        if elm == ".":
            if len(stack) == 1:
                print(f"#{test_case} {stack.pop()}")
            else:
                print(f"#{test_case} error")
            break

        if len(stack) >= 2:
            stack.append(operation(elm, int(stack.pop()), int(stack.pop())))
        else:
            print(f"#{test_case} error")
            break
