class Solution:
    def smallestNumber(self, n: int) -> int:
        while n & (n + 1):
            n |= n + 1
        return n