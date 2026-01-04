class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Solution1 (Brute Force) (Time - O(m*n) Space - O(m+n))
        row_zero = set()
        col_zero = set()
        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]==0:
                    row_zero.add(i)
                    col_zero.add(j)
        for i in range(rows):
            for j in range(cols):
                if i in row_zero or j in col_zero:
                    matrix[i][j]=0