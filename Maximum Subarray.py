class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxs = nums[0]
        summ = 0
        for num in nums:
            if summ <0:
                summ = 0
            summ+=num
            maxs = max(maxs,summ)
        return maxs
