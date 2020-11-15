## 4861 - 회문

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = [input() for _ in range(N)]

    palindrome = ""
    # 가로 회문 찾기
    for row in matrix:
        for idx, alpha in enumerate(row[: len(row) - M + 1]):
            substr = row[idx : idx + M]
            if substr == substr[::-1]:
                palindrome = substr
                break

    # 세로 회문 찾기
    transposed = list(zip(*matrix))
    for col in transposed:
        for jdx, alpha in enumerate(col[: len(col) - M + 1]):
            substr = col[jdx : jdx + M]
            if substr == substr[::-1]:
                palindrome = "".join(substr)
                break

    print(f"#{test_case} {palindrome}")
