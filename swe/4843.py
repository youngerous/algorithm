## 4843 - 특별한 정렬

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = sorted(list(map(int, input().split())))
    result = []
    for i in range(5):
        result.append(arr[len(arr) - i - 1])
        result.append(arr[i])

    print(f'#{test_case} {" ".join(list(map(str, result)))}')
