class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        k = 0
        res = 0
        prices.append(-1)
        if prices[0] <= prices[1]:
            k = prices[0]

        for i in range(1, len(prices) - 1):
            if prices[i] < prices[i - 1]:
                k = prices[i]
            elif prices[i] > prices[i + 1]:
                res += prices[i] - k

        return res