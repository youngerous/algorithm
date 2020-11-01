import sys

input = sys.stdin.readline


def main_1():
    N = int(input())
    nums = [int(input()) for _ in range(N)]
    nums.sort()
    for i in nums:
        print(i)


def main_2():
    sys.stdout.write(
        "\n".join(map(str, sorted(map(int, sys.stdin.read().splitlines()[1:]))))
    ) + "\n"


main_2()
