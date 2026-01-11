class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        i, j = 0, n - 1 # Start Top-Right
        count = 0
        
        while i < m and j >= 0:
            if grid[i][j] < 0:
                # If current is neg, all below in this col are neg
                count += m - i 
                j -= 1 # Move Left
            else:
                # If current is pos, this row is safe, move down
                i += 1 # Move Down
                
        return count