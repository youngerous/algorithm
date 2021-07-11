import collections


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dictionary = collections.defaultdict(int)
        maxlen = 0
        start = 0

        # two-pointer
        for idx, char in enumerate(s):
            if char in dictionary and start <= dictionary[char]:
                # 한 번 등장한 적이 있는 문자도 현재 substring 바깥에 있으면 무시
                start = dictionary[char] + 1
            else:
                maxlen = max(maxlen, idx - start + 1)
            dictionary[char] = idx
        return maxlen