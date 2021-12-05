class Solution:
    # https://github.com/onlybooks/algorithm-interview/issues/104

    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        graph = collections.defaultdict(list)
        for fr, to, price in flights:
            graph[fr].append((to, price))

        Q = [(0, src, k)]  # 가격, 정점, 남은 경유지 수
        visited = [(sys.maxsize, k)] * n

        while Q:
            price, node, remain = heapq.heappop(Q)
            if node == dst:
                return price
            if remain >= 0:
                for to, pr in graph[node]:
                    alt = price + pr
                    if alt < visited[to][0] or remain - 1 >= visited[to][1]:
                        visited[to] = (alt, remain - 1)
                        heapq.heappush(Q, (alt, to, remain - 1))
        return -1