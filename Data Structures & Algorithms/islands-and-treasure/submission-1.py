class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        rows, cols = len(grid), len(grid[0])
        queue = deque()

        def bfs():
            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc

                    if nr not in range(rows) or nc not in range(cols) or grid[nr][nc] == -1: continue

                    if grid[nr][nc] == 2147483647:
                        grid[nr][nc] = grid[r][c]+1
                        queue.append((nr, nc))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0: queue.append((r,c))
                    
        bfs()