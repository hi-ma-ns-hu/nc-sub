class Solution:
  def isMatch(self, s: str, p: str) -> bool:
    
    cache = [[None]*(len(p)+1) for _ in range(len(s)+1)]

    def dfs(i, j):
        # base condition, if j finishes, if i also finished then True
        if j == len(p): return i == len(s)
        if cache[i][j] is not None: return cache[i][j]

        isMatch = i < len(s) and (s[i] == p[j] or p[j] == '.')

        # if next char is *, either skip it or if isMatch use one char from s and keep p at same j
        if (j+1) < len(p) and p[j+1] == '*':
            cache[i][j] = dfs(i, j+2) or (isMatch and dfs(i+1, j))
            return cache[i][j]

        if isMatch:
            cache[i][j] = dfs(i+1, j+1)
            return cache[i][j]

        cache[i][j] = False
        return False

    return dfs(0,0)      