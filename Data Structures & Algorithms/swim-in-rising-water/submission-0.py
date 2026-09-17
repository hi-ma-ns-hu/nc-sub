class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = [[False] * n for _ in range(n)]

        def dfs(r, c, t):
            if r not in range(n) or c not in range(n) or visited[r][c]: return float('inf')
            if r == n-1 and c == n-1: return max(t, grid[r][c])

            visited[r][c] = True
            t = max(t, grid[r][c])
            res = min(dfs(r+1, c, t), dfs(r-1, c, t), dfs(r, c+1, t), dfs(r, c-1, t))
            visited[r][c] = False
            return res

        return dfs(0, 0, 0)