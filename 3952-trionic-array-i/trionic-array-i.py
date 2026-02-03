class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        peak = n - 1
        valley = 0

        for i in range(n - 1):
            if peak == n - 1 and nums[i] >= nums[i + 1]:
                peak = i
            if valley == 0 and nums[-1 - i] <= nums[-2 - i]:
                valley = n - 1 - i
            if peak < valley:
                return self.isDecreasing(nums, peak, valley)

        return False


    def isDecreasing(self, A: List[int], a: int, b: int) -> bool:
        if a == 0 or b == len(A) - 1: return False
        for i in range(a, b):
            if A[i] <= A[i + 1]: return False
        return True
