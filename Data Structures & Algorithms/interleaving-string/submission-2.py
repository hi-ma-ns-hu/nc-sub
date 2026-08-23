class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1)+len(s2) != len(s3): return False

        cache = [[None]*(len(s2)+1) for _ in range(len(s1)+1)]

        def dfs(i, j, k):
            # base condition
            if k == len(s3): return (i == len(s1) and j == len(s2))
            if cache[i][j] is not None: return cache[i][j]
            # if s1[i] == s3[k], recurse through i else recurse through k and if recurse result are true return
            if i < len(s1) and s1[i] == s3[k]:
                if dfs(i+1, j, k+1):
                    cache[i][j] = True
                    return True
            
            if j < len(s2) and s2[j] == s3[k]:
                if dfs(i, j+1, k+1):
                    cache[i][j] = True
                    return True
            
            cache[i][j] = False
            return False

        return dfs(0,0,0) # index for s1, s2 and s3 resp.