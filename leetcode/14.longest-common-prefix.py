#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        common = strs[0]
        check = strs[0]
        for word in strs:
            shorter = check if len(check) < len(word) else word
            isSuccessive = True
            tmpCommon = ""

            for idx in range(len(shorter)):
                if isSuccessive:
                    if check[idx] == word[idx]:
                        tmpCommon += check[idx]
                    else:
                        isSuccessive = False
            common = tmpCommon if len(common) > len(tmpCommon) else common
        return common


# @lc code=end
