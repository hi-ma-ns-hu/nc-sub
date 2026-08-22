class Solution:
  def change(self, amount: int, coins: List[int]) -> int:
    cache = [0]*(amount+1)
    cache[0] = 1

    for i in range(len(coins)-1, -1, -1):
        for j in range(1, amount+1):
            cache[j] += cache[j-coins[i]] if j >= coins[i] else 0

    return cache[amount]