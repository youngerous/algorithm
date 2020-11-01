#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
        }

        result = 0
        for idx in range(len(s) - 1):
            multi = s[idx] + s[idx + 1]
            if multi in roman:
                result += roman[multi]
                result -= roman[s[idx + 1]]
                continue
            result += roman[s[idx]]
        result += roman[s[-1]]
        return result


# @lc code=end
