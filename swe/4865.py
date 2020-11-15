## 4865 - 글자수

T = int(input())

for test_case in range(1, T + 1):
    str1, str2 = input(), input()
    dic = {}
    for key in str2:
        dic.setdefault(key, 0)  # without defaultdict
        dic[key] += 1

    maximum = 0
    for s in str1:
        maximum = max(dic[s], maximum)

    print(f"#{test_case} {maximum}")
