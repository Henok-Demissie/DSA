class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        res=""
        for ch in s:
            if ch.isalnum():
                res+=ch.lower()
        res2=""
        for i in res:
            res2=i + res2
        return res==res2

        