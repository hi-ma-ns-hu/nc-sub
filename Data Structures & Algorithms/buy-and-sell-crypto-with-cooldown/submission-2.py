class Solution:
  def maxProfit(self, prices: List[int]) -> int:

    buy_tom, sell_tom = 0, 0 # profit if you buy/sell tomorrow
    buy_tom_tom = 0 # profit if you buy tomorrow

    for idx in range(len(prices)-1, -1, -1):
        buy = max(buy_tom, sell_tom-prices[idx])
        sell = max(sell_tom, buy_tom_tom+prices[idx])
        buy_tom_tom = buy_tom
        buy_tom = buy
        sell_tom = sell

    return buy_tom
