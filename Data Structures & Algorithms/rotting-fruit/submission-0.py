class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        queue = deque()
        
        res = -1 # so to make it zero from the first rotten zero
        fresh = 0 # to check if any fresh oranges are left or not

        def bfs():
            nonlocal res, fresh
            while queue:
                for _ in range(len(queue)):
                    r, c = queue.popleft()
                    for dr, dc in directions:
                        nr, nc = r+dr, c+dc
                        if nr not in range(rows) or nc not in range(cols) or grid[nr][nc] != 1: continue
                        
                        fresh -= 1
                        grid[nr][nc] = 2
                        queue.append((nr, nc))
                res += 1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1: fresh += 1
                elif grid[r][c] == 2: queue.append((r,c))

        bfs()

        return -1 if fresh else res