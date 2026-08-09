class Solution:
  def climbStairs(self, n: int) -> int:
    one, two = 1, 1 # no of ways 2nd last index and last index could climb
    for _ in range(n-2, -1, -1):
        # one and two both come back steps after each iteration
        temp = one
        one += two
        two = temp
    return one