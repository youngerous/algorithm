#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        rev_x = x[::-1]

        return True if x == rev_x else False


# @lc code=end
