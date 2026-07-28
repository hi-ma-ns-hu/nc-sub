class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(0,1), (0,-1), (1, 0), (-1, 0)]
        rows, cols = len(grid), len(grid[0])
        res = 0

        def dfs(r, c):
            if r not in range(rows) or c not in range(cols) or grid[r][c] == 0: return 0

            grid[r][c] = 0
            area = 1
            for dr, dc in directions:
                area += dfs(r+dr, c+dc)
            return area
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = dfs(r, c)
                    res = max(res, area)
        
        return res