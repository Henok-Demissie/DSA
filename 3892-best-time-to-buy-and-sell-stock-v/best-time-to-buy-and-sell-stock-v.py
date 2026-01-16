class Solution:
    def maximumProfit(self, prices, k):
        n = len(prices)
        NEG = -10**18

        dp = [[[None] * 3 for _ in range(k + 1)] for _ in range(n + 1)]

        def dfs(i, t, state):
            if i == n:
                return 0 if state == 0 else NEG

            if dp[i][t][state] is not None:
                return dp[i][t][state]

            ans = dfs(i + 1, t, state)

            if state == 0:
                ans = max(ans, dfs(i + 1, t, 1) - prices[i])
                ans = max(ans, dfs(i + 1, t, 2) + prices[i])
            elif state == 1 and t < k:
                ans = max(ans, dfs(i + 1, t + 1, 0) + prices[i])
            elif state == 2 and t < k:
                ans = max(ans, dfs(i + 1, t + 1, 0) - prices[i])

            dp[i][t][state] = ans
            return ans

        return dfs(0, 0, 0)