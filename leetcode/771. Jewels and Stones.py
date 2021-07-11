import collections


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_dict = collections.defaultdict(int)
        for jewel in jewels:
            jewel_dict[jewel] += 1

        total = 0
        for stone in stones:
            if stone in jewel_dict.keys():
                total += 1

        return total

    def alternative_answer(self, jewels: str, stones: str) -> int:
        return sum(stone in jewels for stone in stones)