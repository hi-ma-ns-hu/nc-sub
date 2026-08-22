class Solution:
  def maxProfit(self, prices: List[int]) -> int:

    cache = [[-1]*2 for _ in range(len(prices)+1)]
    
    def dfs(idx, can_buy):
        if idx >= len(prices): return 0
        if cache[idx][can_buy] != -1: return cache[idx][can_buy]

        if can_buy:
            cache[idx][can_buy] = max(dfs(idx+1, can_buy), dfs(idx+1, False)-prices[idx]) # total profit reduced because he buyed of prices[idx]
        else:
            cache[idx][can_buy] =  max(dfs(idx+1, can_buy), dfs(idx+2, True)+prices[idx]) # total profit increased because he sold of prices[idx] and idx+2 because since he sold today he will only be able to place the next trade day after tomorrow
        
        return cache[idx][can_buy]

    return dfs(0, True)  