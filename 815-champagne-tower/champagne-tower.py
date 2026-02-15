class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        if query_row == 0:
            return min(1, poured)

        # symmetry: (r, g) == (r, r-g)
        query_glass = min(query_glass, query_row - query_glass)

        # dp[c] = amount in glass c of the current row (not capped at 1)
        # +1 extra so dp[c+1] is always safe to update
        dp = [poured] + [0] * (query_glass + 1)
        for r in range(query_row):
            end = min(r, query_glass)
            dp[end + 1] = 0.0  # rightmost cell of the next row in our tracked region

            next_lo, next_hi = 10**9, -1
            pouring = False

            # Build next row from current in-place
            for c in reversed(range(end + 1)):
                x = dp[c]
                if x > 1.0:  # If we have overflow then pour it to the next row
                    pouring = True
                    overflow = (x - 1.0) * 0.5
                    dp[c] = overflow
                    dp[c + 1] += overflow

                    # Track next glasses that are within 0..query_glass (tracked side)
                    if c < next_lo: next_lo = c
                    if c > next_hi: next_hi = c
                    if c + 1 <= query_glass and c + 1 > next_hi: next_hi = c + 1
                else:  # No overflow, then next row will not
                    dp[c] = 0.0

            # Early stop 1: nothing flows further
            if not pouring:
                return 0.0

            # Early stop 2: query_glass is outside the maximum possible pouring window
            # From [next_lo..next_hi] at row r+1, you can expand by at most 1 per remaining row.
            rem = query_row - (r + 1)
            if query_glass < next_lo - rem or query_glass > next_hi + rem:
                return 0.0

        return min(1, dp[query_glass])