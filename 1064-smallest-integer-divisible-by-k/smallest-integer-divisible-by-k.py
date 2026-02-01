class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if gcd(10, k)>1: return -1
        X=[1, 11, 111, 1111, 11111, 111111]
        l0=bisect.bisect_left(X, k)
        r=X[l0]%k
        len0=l0+1
        if r==0: return len0
        len0+=1
        while True:
            r=(10*r+1)%k
            if r==0: return len0
            len0+=1

        return -1
        