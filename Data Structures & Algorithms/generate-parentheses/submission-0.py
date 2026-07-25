class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = list()
        def dfs(open, close, subset):
            # if open = close then it means it is 2n combined and base condition has been reached
            if open == close == n:
                res.append(''.join(subset))
                return
            
            if open < n:
                subset.append('(')
                dfs(open+1, close, subset)
                subset.pop()
            
            if close < open:
                subset.append(')')
                dfs(open, close+1, subset)
                subset.pop()

        dfs(0, 0, list())
        return res