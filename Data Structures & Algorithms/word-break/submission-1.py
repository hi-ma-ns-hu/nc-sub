class Solution:
  def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    cache = {len(s): True}

    def dfs(index):
        if index in cache: return cache[index]
        # check for every word in wordDict if there is corresponding substr in s
        for word in wordDict:
            # if index+len(word) is less than len(s) word is in s, then we're safe to call next dfs
            if ((index+len(word)) <= len(s)) and word == s[index : index + len(word)]:
                if dfs(index+len(word)):
                    cache[index] = True
                    return True
        
        cache[index] = False
        return False
        
    return dfs(0)