class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(s) < len(t): return 0

        cache = [[-1]*(len(t)+1) for _ in range(len(s)+1)]

        def dfs(i, j):
            if j == len(t): return 1 # all char of t has been consumed, so yes we have achieved the result
            if i == len(s): return 0 # we traversed all char of s but t cant be retrieved
            if cache[i][j] != -1: return cache[i][j]

            res = dfs(i+1, j)
            if s[i] == t[j]:
                res += dfs(i+1, j+1)
            
            cache[i][j] = res
            return res

        return dfs(0,0)