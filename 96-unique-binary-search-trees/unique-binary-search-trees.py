class Solution:
    def numTrees(self, n: int) -> int:
        def dfs(low, high, memo: dict):
            if low > high:
                return 1
            if (low, high) not in memo:
                memo[(low, high)] = 0
                for i in range(low, high+1):
                    memo[(low, high)] += dfs(low, i-1, memo) * dfs(i+1, high, memo)
            return memo[(low, high)]
        return dfs(1, n, {})