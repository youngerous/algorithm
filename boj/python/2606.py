def dfs(row_idx, row):
    global virus
    global network
    global visited

    if sum(row) == 0:
        return
    for idx, rr in enumerate(row):
        visited[row_idx] = True
        if not visited[idx] and rr:
            network[row_idx][idx] = False
            network[idx][row_idx] = False
            virus += 1
            dfs(idx, network[idx])


computers, pairs = int(input()), int(input())
network = [[False for _ in range(computers)] for _ in range(computers)]
visited = [False for _ in range(computers)]
for _ in range(pairs):
    cnt_1, cnt_2 = map(int, input().split())
    network[cnt_1 - 1][cnt_2 - 1] = True
    network[cnt_2 - 1][cnt_1 - 1] = True

virus = 0
dfs(0, network[0])
print(virus)
