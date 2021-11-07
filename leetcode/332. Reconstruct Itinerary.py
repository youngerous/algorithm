class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # 그래프 구성
        # example: {'ATL': ['JFK', 'SFO'], 'JFK': ['ATL', 'SFO'], 'SFO': ['ATL']}
        graph = collections.defaultdict(list)
        for fr, to in sorted(tickets):
            graph[fr].append(to)

        route = []

        def dfs(start):
            while graph[start]:
                dfs(graph[start].pop(0))
            route.append(start)

        dfs("JFK")
        return route[::-1]