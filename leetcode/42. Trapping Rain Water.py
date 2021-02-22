class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        total_rain = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]

        # two-pointer method :: O(n)
        # until reaching maximum height
        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])

            if left_max <= right_max:
                total_rain += left_max - height[left]
                left += 1
            else:
                total_rain += right_max - height[right]
                right -= 1

        return total_rain
