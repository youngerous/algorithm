#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        MAX = 2 ** 31
        result = ""
        x = str(x)

        if "-" in x:
            result = "-"
            x = x[1:]

        x = int("".join(reversed(x)))

        if x < -MAX or x >= MAX:
            return 0

        result += str(x)
        return result


# @lc code=end
