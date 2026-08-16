class Solution:
  def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    def dfs(index):
        if index == len(s): return True
        # check for every word in wordDict if there is corresponding substr in s
        for word in wordDict:
            # if len(word) is less than len(s) word is in s, then we're safe to call next dfs
            if len(word) <= len(s) and word == s[index : index + len(word)]: return dfs(index+len(word))
        return False
    return dfs(0)      