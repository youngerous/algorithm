#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open = ["(", "{", "["]
        close = [")", "}", "]"]

        for each in s:
            if each in open:
                stack.append(each)
            else:
                if len(stack) == 0:
                    return False

                pop = stack.pop()
                if close.index(each) != open.index(pop):
                    return False
        return True if len(stack) == 0 else False


# @lc code=end
