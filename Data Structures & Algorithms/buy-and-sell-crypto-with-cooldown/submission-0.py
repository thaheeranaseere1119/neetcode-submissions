class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        hold = -prices[0]
        sold = 0
        rest = 0
        for i in range(1, n):

            oldHold = hold
            oldSold = sold
            oldRest = rest

            hold = max(oldHold, oldRest - prices[i])

            sold = oldHold + prices[i]

            rest = max(oldRest, oldSold)

        return max(sold, rest)