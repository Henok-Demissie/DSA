class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)

        balance = [0] * n  # first-occurrence markers for current l
        first = dict()  # val -> first occurence idx for current l

        result = 0
        for l in reversed(range(n)):
            x = nums[l]

            # If x already had a first occurrence to the right, remove that old marker.
            if x in first:
                balance[first[x]] = 0

            # Now x becomes first occurrence at l.
            first[x] = l
            balance[l] = 1 if (x & 1) == 0 else -1

            # Find rightmost r >= l such that sum(balance[l..r]) == 0
            s = 0
            for r in range(l, n):
                s += balance[r]
                if s == 0:
                    result = max(result, r - l + 1)

        return result