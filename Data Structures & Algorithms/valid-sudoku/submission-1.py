class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rs = [set() for _ in range(9)]
        cs = [set() for _ in range(9)]
        bs = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):

                if board[i][j] == '.':
                    continue

                # using i and j, just find the box number where you currently are
                box = (i//3)*3+(j//3) # box number from (i,j)

                if board[i][j] in rs[i] or board[i][j] in cs[j] or board[i][j] in bs[box]:
                    return False

                rs[i].add(board[i][j])
                cs[j].add(board[i][j])
                bs[box].add(board[i][j])
        return True