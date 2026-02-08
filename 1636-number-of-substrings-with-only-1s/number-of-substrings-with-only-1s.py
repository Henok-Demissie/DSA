class Solution:
    def numSub(self, s: str) -> int:
        cnt = 0
        for part in s.split('0'):
            n = len(part)
            cnt += n*(n+1)

        return (cnt // 2) % (10**9 + 7)