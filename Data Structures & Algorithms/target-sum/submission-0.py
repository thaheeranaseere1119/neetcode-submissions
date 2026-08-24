class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if abs(target) > total:
            return 0
        dp = {0: 1}
        for num in nums:
            new_dp = {}
            for total_sum in dp:
                new_dp[total_sum + num] = new_dp.get(total_sum + num, 0) + dp[total_sum]
                new_dp[total_sum - num] = new_dp.get(total_sum - num, 0) + dp[total_sum]
            dp = new_dp
        return dp.get(target, 0)