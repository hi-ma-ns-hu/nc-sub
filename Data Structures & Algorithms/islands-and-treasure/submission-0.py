class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        rows, cols = len(grid), len(grid[0])
        
        def dfs(r, c, distance):
            if r not in range(rows) or c not in range(cols) or grid[r][c] < distance: return

            grid[r][c] = distance
            for dr, dc in directions:
                dfs(dr+r, dc+c, distance+1)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0: dfs(r, c, 0)