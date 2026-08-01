class Solution:
  def orangesRotting(self, grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    directions = [(1,0), (0,1), (-1, 0), (0, -1)]

    from collections import deque
    queue = deque()

    res = 0
    fresh = 0

    def bfs():
      nonlocal res, fresh
      while queue:
        for _ in range(len(queue)):
          r, c = queue.popleft()
          for dr, dc in directions:
            nr, nc = r+dr, c+dc
            if nr not in range(rows) or nc not in range(cols) or grid[nr][nc] != 1: continue

            grid[nr][nc] = 2
            fresh -= 1
            queue.append((nr, nc))
        if queue: res += 1

    for r in range(rows):
      for c in range(cols):
        if grid[r][c] == 1:
          fresh += 1
        if grid[r][c] == 2:
          queue.append((r,c))

    if fresh == 0: return 0

    bfs()
    print(fresh, res,)
    return res if fresh == 0 else -1