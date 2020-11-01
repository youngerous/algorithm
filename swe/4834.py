## 4834 - 숫자 카드

T = int(input())

for test_case in range(1, T + 1):
    N, cards = int(input()), input()
    countdict = {key: 0 for key in set(cards)}

    for card in cards:
        countdict[card] += 1

    max_val = max(countdict.values())
    max_key = max([key for key in countdict.keys() if countdict[key] == max_val])
    print("#{} {} {}".format(test_case, max_key, max_val))
