class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pp = float('inf')
        profit = 0

        for i in prices:
            pp = min(pp, i)
            profit = max(profit, i-pp)
        return profit