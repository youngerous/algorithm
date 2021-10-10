class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(csum, index, path):
            if csum < 0:  # prevent searching unlimited number of times
                return
            if csum == 0:  # exact match
                result.append(path)
                return

            for idx in range(index, len(candidates)):
                dfs(csum - candidates[idx], idx, path + [candidates[idx]])

        dfs(target, 0, [])
        return result