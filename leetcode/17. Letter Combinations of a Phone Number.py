class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(start, path):
            """
            Example:
                digits = "245"
                dfs:
                    1. Find all combinations of "245"
                    2. Find all combinations of "45"
                    3. Find all combinations of "5"
            """
            # end condition
            if len(path) == len(digits):
                combi.append(path)
                return

            # recursive
            for idx in range(start, len(digits)):
                for word in mapping[digits[idx]]:
                    dfs(idx + 1, path + word)

        if not digits:
            return []
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        combi = []
        dfs(0, "")

        return combi
