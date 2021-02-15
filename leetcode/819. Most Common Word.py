import re
from collections import defaultdict, Counter


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # substitute all symbols into whitespace and remove banned words
        words = [
            word
            for word in re.sub(r"[^\w]", " ", paragraph).lower().split()
            if word not in banned
        ]

        # count words and return most common word
        counts = Counter(words)
        return counts.most_common(1)[0][0]

        ## Second Solution (using defaultdict)
        # counts = defaultdict(int)
        # for word in words:
        #     counts[word] += 1
        # return max(counts, key=count.get)
