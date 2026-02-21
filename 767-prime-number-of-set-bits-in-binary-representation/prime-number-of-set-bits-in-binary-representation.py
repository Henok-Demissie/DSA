class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        return sum((1<<x.bit_count())&((1<<2)|(1<<3)|(1<<5)|(1<<7)|(1<<11)|(1<<13)|(1<<17)|(1<<19))>0 for x in range(left, right+1) )