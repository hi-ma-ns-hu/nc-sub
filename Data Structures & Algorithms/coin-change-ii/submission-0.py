class Solution:
  def change(self, amount: int, coins: List[int]) -> int:

    def dfs(idx, amount):

        if idx >= len(coins): return 0
        if amount == coins[idx]: return 1
        
        # we only proceed if amount >= coins[idx]
        res = 0
        if amount >= coins[idx]:
            # either select the coins at current index or skip it
            select_curr_coin = dfs(idx, amount-coins[idx])
            skip_curr_coin = dfs(idx+1, amount)
            res += select_curr_coin + skip_curr_coin

        return res

    return dfs(0, amount)