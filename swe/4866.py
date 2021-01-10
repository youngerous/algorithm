## 4866 - 괄호검사

T = int(input())

for test_case in range(1, T + 1):
    code = input()

    stack = []
    opened = {"{": 0, "(": 1}
    closed = {"}": 0, ")": 1}
    for char in code:
        if char in opened:
            stack.append(char)
        elif char in closed:
            if not stack:
                stack.append(char)
                break
            if not opened[stack[-1]] == closed[char]:
                break
            stack.pop()

    result = 0 if stack else 1

    print(f"#{test_case} {result}")

