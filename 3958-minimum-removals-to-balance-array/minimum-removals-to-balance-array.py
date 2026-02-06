class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()

        l = maxsize = 0
        for r in range(len(nums)):
            while nums[r] / nums[l] > k:
                l += 1
            if r - l + 1 > maxsize:
                maxsize = r - l + 1

        return len(nums) - maxsize