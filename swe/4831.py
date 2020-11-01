## 4831 - 전기버스

T = int(input())

for test_case in range(1, T + 1):
    K, N, M = map(int, input().split())
    stops = list(map(int, input().split()))  # 충전소가 설치된 장소

    fuel = K  # 잔여 연료
    previous = 0  # 현재 충전소에 도착하기 직전의 위치
    count = 0  # 충전 횟수
    possible = True  # 끝까지 도달 가능한지 판단하는 flag

    # [1] 모든 "충전소"를 방문한다.
    for idx, stop in enumerate(stops):

        # [2] 이동한 거리만큼 연료를 감소시키고, previous를 현재 위치로 설정한다.
        fuel -= stop - previous
        previous = stop

        # [2-1] 가장 가까운 충전소에도 도달하지 못한다면, 0을 출력한다.
        if fuel < 0:
            possible = False
            break

        # [3] (마지막 충전소 제외) 다음 충전소까지 갈 수 있는지 확인한다
        # [3-1] 갈 수 있다면, 다음 충전소로 이동한다.
        if idx < len(stops) - 1 and stops[idx + 1] - stop <= fuel:
            continue

        # [3-2] 갈 수 없다면, 현재 충전소에서 충전한다.
        # [3-2-1] 마지막 충전소일 경우, 종점까지 갈 수 있다면 종점으로 곧장 이동한다.
        if idx == len(stops) - 1 and N - stop <= fuel:
            continue
        fuel = K
        count += 1

    print("#{} {}".format(test_case, count)) if possible else print(
        "#{} 0".format(test_case)
    )
