## 4873 - 반복문자 지우기

T = int(input())
for test_case in range(1, T + 1):
    string = input()
    stack = []
    for s in string:
        if not stack:  # 바깥에서 처리하면 memory error
            stack.append(s)
            continue
        stack.pop() if stack[-1] == s else stack.append(s)

    print(f"#{test_case} {len(stack)}")
