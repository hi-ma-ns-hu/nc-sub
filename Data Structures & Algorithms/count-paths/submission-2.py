class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = [1]*n
        
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                cache[j] += cache[j+1]
        
        return cache[0]