class Solution:
  def isValidSudoku(self, board: List[List[str]]) -> bool:
    rows, cols = len(board), len(board[0])
    row_set = defaultdict(set)
    col_set = defaultdict(set)
    sq_set = defaultdict(set)

    for r in range(rows):
      for c in range(cols):
        if board[r][c] != '.':
          if board[r][c] in row_set[r] or board[r][c] in col_set[c] or board[r][c] in sq_set[(r//3,c//3)]:
            return False
          row_set[r].add(board[r][c])
          col_set[c].add(board[r][c])
          sq_set[(r//3,c//3)].add(board[r][c])
    return True