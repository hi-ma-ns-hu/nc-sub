class Solution:
  def coinChange(self, coins: List[int], amount: int) -> int:

    def dfs(amount):
      if amount == 0: return 0
      res = 10_000_000
      for i in coins:
        if amount - i >= 0:
          res = min(res, 1+dfs(amount-i))
      return res

    res = dfs(amount)
    return -1 if res >= 10_000_000 else res