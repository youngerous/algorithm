## 4835 - 구간합

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    minsum, maxsum = float("inf"), 0
    for idx, _ in enumerate(nums[: -M + 1]):
        neighbors = 0
        for jdx in range(M):
            neighbors += nums[idx + jdx]
        if neighbors < minsum:
            minsum = neighbors
        if neighbors > maxsum:
            maxsum = neighbors
    print("#{} {}".format(test_case, maxsum - minsum))
