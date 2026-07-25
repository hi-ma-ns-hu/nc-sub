class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = list()
        
        def dfs(index, subset, col_set, neg_diag, pos_diag):
            if index >= n:
                res.append([''.join(r) for r in subset])
                return

            # we've row (index), lets explore columns
            for c in range(n):
                # for positive diag: our r+c is always same as n-1 and similarly for -ve diag: r-c is alway same as 0
                # so we're maintaining +ve and -ve diagonal set along with col_set, row is not managed because thats
                # always going to be one at a time in dfs params
                if c in col_set or (index-c) in neg_diag or (index+c) in pos_diag:
                    continue
                col_set.add(c)
                neg_diag.add(index-c)
                pos_diag.add(index+c)
                subset[index][c] = 'Q'
                # include
                dfs(index+1, subset, col_set, neg_diag, pos_diag)
                # backtrack
                col_set.remove(c)
                neg_diag.remove(index-c)
                pos_diag.remove(index+c)
                subset[index][c] = '.'
            
        dfs(0, [['.']*n for _ in range(n)], set(), set(), set())

        return res