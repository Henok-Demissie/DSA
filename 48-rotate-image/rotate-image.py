from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        # Step 1: **Transpose** the matrix
        # Swap elements across the main diagonal
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: **Reverse** each row
        # Use slicing to reverse each row
        for i in range(n):
            matrix[i].reverse()