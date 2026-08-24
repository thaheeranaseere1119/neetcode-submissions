class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProd = nums[0]
        minProd = nums[0]
        answer = nums[0]

        for i in range(1, len(nums)):
            oldMax = maxProd
            oldMin = minProd
            maxProd = max(
                nums[i],
                nums[i] * oldMax,
                nums[i] * oldMin
            )
            minProd = min(
                nums[i],
                nums[i] * oldMax,
                nums[i] * oldMin
            )
            answer = max(answer, maxProd)
        return answer