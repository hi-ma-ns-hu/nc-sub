class Solution:
    def is_palindrome(self, s):
        l, r = 0, len(s)-1
        while l < r:
            if s[l] != s[r]:
                return False
            l = l+1
            r = r-1
        return True

    def partition(self, s: str) -> List[List[str]]:
        res = list()

        def dfs(index, subset):
            if index >= len(s):
                res.append(subset[:])
                return
            
            # this is case of permutation, so use for loop
            for i in range(index, len(s)):
                if self.is_palindrome(s[index : i+1]):
                    subset.append(s[index : i+1])
                    dfs(i+1, subset)
                    subset.pop()

        dfs(0, [])
        return res 
        