class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps=0
        farthest=0
        current=0
        for i in range(len(nums)-1):
            farthest=max(farthest,nums[i]+i)
            if i==current:
                jumps+=1
                current=farthest
        return jumps

