class Solution:
  def coinChange(self, coins: List[int], amount: int) -> int:

    if amount == 0: return 0

    queue = deque([0]) # starting amount
    visited = [False]*(amount+1)
    visited[0] = True
    res = 0 # number of steps in bfs

    while queue:
      res += 1
      for _ in range(len(queue)):
        curr_amt = queue.popleft()
        for i in coins:
          new_amt = curr_amt+i
          if new_amt == amount: return res
          if new_amt > amount or visited[new_amt]: continue
          visited[new_amt] = True
          queue.append(new_amt)
    return -1