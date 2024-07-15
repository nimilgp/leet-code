class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        low = prices[0]
        for price in prices:
            if price < low:
                low = price
            profit = max(profit, price - low)
        return profit
