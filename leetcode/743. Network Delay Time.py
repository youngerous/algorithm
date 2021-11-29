class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # construct adjacency graph
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        # construct queue (time, vertex)
        Q = [(0, k)]
        dist = collections.defaultdict(int)

        # dijkstra
        while Q:
            time, node = heapq.heappop(Q)
            if node not in dist:  # not visited
                dist[node] = time
                for v, w in graph[node]:
                    alt = time + w
                    heapq.heappush(Q, (alt, v))

        # whether every node is visited
        if len(dist) == n:
            return max(dist.values())
        return -1