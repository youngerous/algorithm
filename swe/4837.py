## 4837 - 부분집합의 합

T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    count = 0

    # 모든 부분집합에 대해 확인
    A = list(range(1, 13))
    for i in range(1 << len(A)):
        # 부분집합 생성
        tmp = []
        for j in range(len(A)):
            if i & (1 << j):
                tmp.append(A[j])
        # 조건 확인
        if len(tmp) == N and sum(tmp) == K:
            count += 1

    print("#{} {}".format(test_case, count))
