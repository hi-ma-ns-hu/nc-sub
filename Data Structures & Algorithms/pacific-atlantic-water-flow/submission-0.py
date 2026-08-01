from typing import List

class Solution:
  def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
    rows, cols = len(heights), len(heights[0])
    directions = [(1,0), (0,1), (-1,0), (0,-1)]
    pacific, atlantic = set(), set()
    res = list()

    def dfs(r, c, visited, prev_height):
      if r not in range(rows) or c not in range(cols) or (r,c) in visited or heights[r][c] < prev_height: return

      visited.add((r,c))

      for dr, dc in directions:
        dfs(r+dr, c+dc, visited, heights[r][c])

    # since top-left are pacific and bottom-right are atlantic
    # start from each of the border cell

    # visits for the top and bottom borders row
    for c in range(cols):
      dfs(0, c, pacific, heights[0][c])
      dfs(rows-1, c, atlantic, heights[rows-1][c])

    for r in range(rows):
      dfs(r, 0, pacific, heights[r][0])
      dfs(r, cols-1, atlantic, heights[r][cols-1])

    for r in range(rows):
      for c in range(cols):
        if (r, c) in pacific and (r,c) in atlantic:
          res.append([r,c])

    return res

sol = Solution()
grid = [[1],[1]]
# [[0,2],[0,4],[1,0],[1,1],[1,2],[1,3],[1,4],[2,0]]
print(sol.pacificAtlantic(heights=grid))