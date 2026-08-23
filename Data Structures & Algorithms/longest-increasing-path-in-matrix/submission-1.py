class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        cache = [[-1]*(cols+1) for _ in range(rows+1)]

        def dfs(r, c, prev_val):
            # base case : out of bound and val matching
            if r not in range(rows) or c not in range(cols) or matrix[r][c] <= prev_val: return 0

            if cache[r][c] != -1: return cache[r][c]

            # a matrix node always by default creates a path of length 1
            res = 1
            for dr, dc in directions:
                res = max(res, 1+dfs(r+dr, c+dc, matrix[r][c]))

            cache[r][c] = res
            return res


        res = 0
        for r in range(rows):
            for c in range(cols):
                res = max(res, dfs(r, c, float('-inf')))
        return res