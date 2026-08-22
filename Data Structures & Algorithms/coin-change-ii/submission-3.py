class Solution:
  def change(self, amount: int, coins: List[int]) -> int:
    coins.sort()
    cache = [[-1]*(amount+1) for _ in range(len(coins)+1)]

    def dfs(idx, amount):
        
        if amount == 0: return 1
        if idx >= len(coins): return 0
        if cache[idx][amount] != -1: return cache[idx][amount]
        
        # we only proceed if amount >= coins[idx]
        res = 0
        if amount >= coins[idx]:
            # either select the coins at current index or skip it
            select_curr_coin = dfs(idx, amount-coins[idx])
            skip_curr_coin = dfs(idx+1, amount)
            res += select_curr_coin + skip_curr_coin
        
        cache[idx][amount] = res

        return res

    return dfs(0, amount)