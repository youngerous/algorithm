from sys import stdin

input = stdin.readline


def ans():
    n = input().rstrip()
    N, size = int(n), len(n)
    if size == 1:
        return N

    total = 0
    for s in range(1, size):
        total += s * (9 * (10 ** (s - 1)))
    # N에서 나머지를 구하는 것이 아니라 빼야 함(200대로 넘어갈 때 반례)
    total += size * (N - (10 ** (size - 1)) + 1)
    return total


if __name__ == "__main__":
    print(ans())
