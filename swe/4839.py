## 4839 - 이진탐색


def binarysearch(start, end, answer, cnt):
    if start > end:
        return False
    mid = (start + end) // 2
    if answer == mid:
        return cnt
    elif answer > mid:
        # index가 아닌 값 자체를 넘겨줄 때에는 mid+1 하면 안됨
        return binarysearch(mid, end, answer, cnt + 1)
    else:
        return binarysearch(start, mid, answer, cnt + 1)


T = int(input())

for test_case in range(1, T + 1):
    p, pa, pb = map(int, input().split())

    winner = 0
    cnt_a = binarysearch(1, p, pa, 0)
    cnt_b = binarysearch(1, p, pb, 0)

    if cnt_a < cnt_b:
        winner = "A"
    elif cnt_a > cnt_b:
        winner = "B"

    print(f"#{test_case} {winner}")
