## 4864 - 문자열 비교

from collections import defaultdict


def boyer_moore(whole: str, pattern: str, jump: defaultdict) -> int:
    if len(whole) < len(pattern):
        return 0

    idx = len(pattern) - 1
    if pattern[idx] != whole[idx]:
        return boyer_moore(whole[jump[whole[idx]] :], pattern, jump)
    else:
        for kdx, jdx in enumerate(range(idx, -1, -1)):
            if pattern[jdx] != whole[jdx]:
                ## aaaaa / aaabaaaabaaaaab 의 반례 해결 (using kdx)
                return boyer_moore(whole[jump[whole[jdx]] - kdx :], pattern, jump)
        return 1


T = int(input())
for test_case in range(1, T + 1):
    str1, str2 = input(), input()

    # pattern setup
    jump = defaultdict(lambda: len(str1))  ## 패턴 외 경우에 대해서는 len(str1)-1
    for i, c in enumerate(str1[::-1]):
        if c not in jump:  ## 이 조건을 체크해야 올바른 jump 가능
            jump[c] = i

    # pattern matching
    print(f"#{test_case} {boyer_moore(str2, str1, jump)}")
