## 4836 - 색칠하기

T = int(input())

for test_case in range(1, T + 1):
    squares = int(input())
    coord = [set(), set()]  # red, blue

    for _ in range(squares):
        x1, y1, x2, y2, color = map(int, input().split())
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                coord[color - 1].add((x, y))

    count = len(coord[0] & coord[1])
    print("#{} {}".format(test_case, count))
