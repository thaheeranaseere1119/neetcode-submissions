class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num = set(nums)
        long = 0

        for n in num:
            if n - 1 not in num:
                count = 1

                while n + count in num:
                    count += 1

                long = max(long, count)

        return long