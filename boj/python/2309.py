from sys import stdin

input = stdin.readline


def main():
    dwarves = list(map(int, stdin.read().splitlines()))
    dwarves.sort()
    for d_1 in dwarves:
        for d_2 in dwarves:
            if sum(dwarves) - (d_1 + d_2) == 100:
                for dwarf in dwarves:
                    if (dwarf != d_1) and (dwarf != d_2):
                        print(dwarf)
                return


if __name__ == "__main__":
    main()
