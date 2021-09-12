class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations = []

        def dfs(nlist, start, k):
            if k == 0:
                combinations.append(nlist[:])
                return

            for num in range(start, n + 1):
                nlist.append(num)
                dfs(nlist, num + 1, k - 1)
                nlist.pop()

        dfs([], 1, k)
        return combinations