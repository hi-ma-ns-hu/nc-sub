class Solution:
    def checkValidString(self, s: str) -> bool:
        cache = [[None]*(len(s)+1) for _ in range(len(s)+1)]
        def dfs(idx, open):
            if open < 0: return False # this means we have close > open
            if idx == len(s): return open == 0 # if we reach the end of string and we've no open, then its true
            if cache[idx][open] is not None: return cache[idx][open]

            if s[idx] == '(':
                result = dfs(idx+1, open+1) # we've new open, our open increase by 1
            elif s[idx] == ')':
                result = dfs(idx+1, open-1) # we've close, then our open decrease by 1
            else:
                result = dfs(idx+1, open+1) or dfs(idx+1, open-1) or dfs(idx+1, open) # this means our current char is '*' and we it can either be ope. ie. increase open by 1, or close i.e. decrease by 1, or '' i.e. open remains same

            cache[idx][open] = result
            return result

        return dfs(0, 0) # start from index 0, and total count of open: