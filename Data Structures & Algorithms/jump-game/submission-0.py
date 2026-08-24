class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach=0
        farthest=0
        for i in range(len(nums)):
            if i>farthest:
                return False
            farthest=max(farthest,nums[i]+i)
        return True
        