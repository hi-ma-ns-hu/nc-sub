class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache = [[0]*((len(text2))+1) for _ in range(len(text1)+1)]

        def dfs(i, j):
            if i == len(text1) or j == len(text2): return 0
            if text1[i] == text2[j]: return 1+dfs(i+1, j+1)
            if cache[i][j] != 0: return cache[i][j]

            cache[i][j] = max(dfs(i+1, j), dfs(i, j+1))
            return cache[i][j]

        return dfs(0, 0)