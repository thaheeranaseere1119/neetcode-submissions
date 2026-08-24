class Solution:
    def trap(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        water=0
        lmax=0
        rmax=0
        while left<right:
            if height[left]<=height[right]:
                if lmax<=height[left]:
                    lmax=height[left]
                else:
                    water+=lmax-height[left]
                left+=1
            else:
                if rmax<=height[right]:
                    rmax=height[right]
                else:
                    water+=rmax-height[right]
                right-=1
        return water
            


        