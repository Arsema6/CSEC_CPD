class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)
        prefmult,postmult = 1,1
        for i in range(len(nums)):
            res[i] = prefmult
            prefmult*= nums[i]
        for i in range(len(nums)-1,-1,-1):
            res[i] *= postmult
            postmult*= nums[i]
        return res
        
