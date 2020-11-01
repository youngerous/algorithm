from sys import stdin

input = stdin.readline


def ans_1():
    N = int(input())
    words = set()
    for _ in range(N):
        words.add(input().strip())

    words = list(words)  # 중복 제거 후 리스트로 변경
    words.sort()  # 사전 순으로 정렬
    words = sorted(words, key=lambda w: len(w))  # 길이 순으로 재정렬

    print("\n".join(words))


def ans_2():
    N = int(input())
    words = []
    for _ in range(N):
        words.append(input().strip())

    words = sorted(set(words))
    MAX_WORDS = 51

    for i in range(MAX_WORDS):
        for word in words:
            if len(word) == i:
                print(word)


ans_1()
