class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []

        # product of left
        product = 1
        for idx in range(len(nums)):
            result.append(product)
            product *= nums[idx]

        # result: [1, 1, 2, 6]

        # product of right
        product = 1
        for idx in range(len(nums) - 1, -1, -1):
            result[idx] *= product
            product *= nums[idx]
        # result: [24, 12, 8, 6]

        return result
