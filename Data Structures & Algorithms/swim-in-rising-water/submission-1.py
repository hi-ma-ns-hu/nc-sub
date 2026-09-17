class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        heap = [(grid[0][0], 0, 0)] # starting out time=grid[0][0], r=0, c=0
        visited = set()

        while heap:
            t, r, c = heapq.heappop(heap)

            if (r, c) in visited: continue

            visited.add((r, c))

            if r == n-1 and c == n-1: return t

            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if nr not in range(n) or nc not in range(n) or (nr, nc) in visited: continue
                heapq.heappush(heap, (max(t, grid[nr][nc]),nr, nc))


