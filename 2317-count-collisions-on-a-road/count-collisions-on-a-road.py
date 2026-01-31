class Solution:
    def countCollisions(self, directions: str) -> int:
        n = len(directions)
        ans, l, r = 0, 0, n - 1
        while l < n and directions[l] == 'L': l += 1
        while r >= l and directions[r] == 'R': r -= 1
        for i in range(l, r + 1):
            if directions[i] != 'S': ans += 1
        return ans