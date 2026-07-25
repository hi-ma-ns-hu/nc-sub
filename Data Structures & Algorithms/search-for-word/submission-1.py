class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        
        def dfs(r, c, i, subset):
            # i == len(word) means every char of word has matched
            if i == len(word): return True

            if (r < 0 or c < 0 or r >= rows or c >= cols or
                (r,c) in subset or # (r,c) in subset means this cell has already been visited
                word[i] != board[r][c]): return False

            subset.add((r,c))
            # include
            res = (dfs(r+1, c, i+1, subset) or
            dfs(r-1, c, i+1, subset) or
            dfs(r, c+1, i+1, subset) or
            dfs(r, c-1, i+1, subset))
            # backtract
            subset.remove((r,c))
            
            return res

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0, set()): return True

        return False
