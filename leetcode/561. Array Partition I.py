class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # get sorted array
        nums.sort()

        # make pairs
        maximized_sum = 0
        for idx in range(0, len(nums) - 1, 2):
            maximized_sum += nums[idx]
        return maximized_sum

        ## one-line solution
        # return sum(sorted(nums))[::2]
