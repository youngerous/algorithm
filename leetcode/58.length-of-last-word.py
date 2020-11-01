#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if s is None:
            return 0
        s = s.strip()
        result = s.split(" ")
        return len(result[-1])


# @lc code=end
