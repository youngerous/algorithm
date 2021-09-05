class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        prev_nums = []

        def dfs(elements):
            if len(elements) == 0:
                results.append(prev_nums[:])

            for elem in elements:
                next_nums = elements[:]
                next_nums.remove(elem)

                prev_nums.append(elem)
                dfs(next_nums)
                prev_nums.pop()

        dfs(nums)
        return results
