class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        rows_zero, cols_zero = [False]*rows, [False]*cols # storing which rows and cols would be zero's

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    rows_zero[r] = True
                    cols_zero[c] = True
        
        # update the matrix
        for r in range(rows):
            for c in range(cols):
                if rows_zero[r] or cols_zero[c]:
                    matrix[r][c] = 0
        