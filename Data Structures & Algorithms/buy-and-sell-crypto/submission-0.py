class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxpro = 0
        minbuy = prices[0]

        for sell in prices:
            maxpro = max(maxpro, sell - minbuy)
            minbuy = min(minbuy, sell)

        return maxpro