class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        current = 0
        farthest = 0
        jumps = 0
        for i in range(n-1):
            farthest = max(farthest, nums[i] + i)
            if i == current:
                jumps += 1
                current = farthest
        return jumps