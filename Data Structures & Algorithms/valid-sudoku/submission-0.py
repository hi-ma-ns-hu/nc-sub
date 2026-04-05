class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # traverse row
        for i in range(len(board)):
            s = set()
            for j in range(len(board[i])):
                if board[i][j] != '.':
                    if board[i][j] in s:
                        return False
                    s.add(board[i][j])
        

        # traverse col
        for i in range(len(board)):
            s = set()
            for j in range(len(board[i])):
                if board[j][i] != '.':
                    if board[j][i] in s:
                        return False
                    s.add(board[j][i])

        # 3*3 traversal
        for i in range(0, len(board), 3):
            for j in range(0, len(board), 3):
                s = set()
                for k in range(i, i+3):
                    for l in range(j, j+3):
                        if board[k][l] != '.':
                            if board[k][l] in s:
                                return False
                            s.add(board[k][l])

        return True