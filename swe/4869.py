## 4869 - 종이붙이기


def checkblock(length, total):
    if length == total:
        return 1
    if length > total:
        return 0
    return checkblock(length + 10, total) + checkblock(length + 20, total) * 2


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    # 마지막에 올 수 있는 블록: 3가지 경우
    # 1. 10짜리 세로블록 1개
    # 2. 20짜리 블록 1개 또는 10짜리 가로블록 2개
    # 점화식: f(n) = f(n-10) + 2 * f(n-20)
    num_papers = checkblock(0, N)
    print(f"#{test_case} {num_papers}")

