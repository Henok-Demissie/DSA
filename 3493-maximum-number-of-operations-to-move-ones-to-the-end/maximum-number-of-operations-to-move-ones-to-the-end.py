class Solution:
    def maxOperations(self, s: str) -> int:
        cnt, n, cnt1, prev=0, len(s), 0, '@'
        for c in s:
            cnt1+=c=='1'
            cnt+=(-(c=='0' and prev=='1'))&cnt1
            prev=c
        return cnt