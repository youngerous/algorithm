class Solution:
    def canFinish_slow(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for key, val in prerequisites:
            graph[key].append(val)

        traced = set()

        def dfs(node):
            if node in traced:
                return False

            traced.add(node)
            for path in graph[node]:
                if not dfs(path):
                    return False
            traced.remove(node)
            return True

        for key in list(graph):
            if not dfs(key):
                return False

        return True

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for key, val in prerequisites:
            graph[key].append(val)

        traced = set()
        visited = set()  ##

        def dfs(node):
            if node in traced:
                return False
            if node in visited:  ##
                return True

            traced.add(node)
            for path in graph[node]:
                if not dfs(path):
                    return False
            traced.remove(node)
            visited.add(node)  ##

            return True

        for key in list(graph):
            if not dfs(key):
                return False

        return True