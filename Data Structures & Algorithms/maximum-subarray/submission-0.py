class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current=nums[0]
        maxsub=nums[0]
        for i in range(1,len(nums)):
            current=max(nums[i],nums[i]+current)
            maxsub=max(maxsub,current)
        return maxsub
        