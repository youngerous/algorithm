class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        waiting = [0] * len(T)

        stack = []
        for idx, temp in enumerate(T):
            while stack and T[stack[-1]] < temp:
                last = stack.pop()
                waiting[last] = idx - last
            stack.append(idx)

        return waiting
