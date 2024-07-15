class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        profit = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit += prices[r] - prices[l]
            l = r
            r += 1
        return profit
