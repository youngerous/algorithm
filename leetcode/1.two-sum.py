#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx, num in enumerate(nums):
            if target - num in nums:
                jdx = nums.index(target - num)
                if idx != jdx:
                    return idx, nums.index(target - num)


# @lc code=end
