class Solution:
    def isMagic(self, grid: List[List[int]], r: int, c: int) -> bool:
        # Step 1: Check Uniqueness and Range (1-9)
        seen = [0] * 10
        
        for i in range(r, r + 3):
            for j in range(c, c + 3):
                val = grid[i][j]
                if val < 1 or val > 9 or seen[val]:
                    return False
                seen[val] = 1
        
        # Step 2: Check Sums
        # Row 1
        if grid[r][c] + grid[r][c + 1] + grid[r][c + 2] != 15: return False
        # Row 3
        if grid[r + 2][c] + grid[r + 2][c + 1] + grid[r + 2][c + 2] != 15: return False
        
        # Col 1
        if grid[r][c] + grid[r + 1][c] + grid[r + 2][c] != 15: return False
        # Col 3
        if grid[r][c + 2] + grid[r + 1][c + 2] + grid[r + 2][c + 2] != 15: return False
        
        # Diagonal 1
        if grid[r][c] + grid[r + 1][c + 1] + grid[r + 2][c + 2] != 15: return False
        # Diagonal 2
        if grid[r + 2][c] + grid[r + 1][c + 1] + grid[r][c + 2] != 15: return False
        
        return True

    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        if m < 3 or n < 3:
            return 0
            
        count = 0
        # Iterate up to m-3 (inclusive in loop logic, so range goes to m-2)
        for i in range(m - 2):
            for j in range(n - 2):
                # Optimization: Center must be 5
                if grid[i + 1][j + 1] != 5:
                    continue
                
                if self.isMagic(grid, i, j):
                    count += 1
                    
        return count