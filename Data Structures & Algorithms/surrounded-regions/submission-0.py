class Solution:
  def solve(self, board: List[List[str]]) -> None:
    directions = [(1,0), (0,1), (-1, 0), (0,-1)]
    rows, cols = len(board), len(board[0])

    # find 'O' regions which aren't surrounded, they are border regions and mark them to 'U'
    def dfs(r,c):
      if r not in range(rows) or c not in range(cols) or board[r][c] != 'O': return

      board[r][c] = 'U'
      for dr, dc in directions:
        dfs(dr+r, dc+c)

    for r in range(rows):
      for c in range(cols):
        if board[r][c] == 'O' and (r in (0, rows-1) or c in (0, cols-1)): dfs(r, c)

    print(board)
    # convert surrounded region to X
    for r in range(rows):
      for c in range(cols):
        if board[r][c] == 'O': board[r][c] = 'X'

    # mark 'U' back to 'O'
    for r in range(rows):
      for c in range(cols):
        if board[r][c] == 'U': board[r][c] = 'O'
