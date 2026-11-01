class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        count = {}

        for i in nums:
            count[i] = count.get(i, 0) + 1

        res = []

        for i in count:
            if count[i] > len(nums) // 3:
                res.append(i)

        return res