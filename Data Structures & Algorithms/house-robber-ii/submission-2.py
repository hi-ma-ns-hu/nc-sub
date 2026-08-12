class Solution:
  def rob(self, nums: List[int]) -> int:
    memo = [[-1]*2 for _ in range(len(nums))]
    if len(nums) == 1: return nums[0]
    def dfs(index, flag):
        if index >= len(nums) or (flag and index == len(nums)-1): return 0
        if memo[index][flag] != -1: return memo[index][flag]
        memo[index][flag] = max(dfs(index+2, flag or index == 0)+nums[index],dfs(index+1, flag))
        return memo[index][flag]
    return max(dfs(0, True), dfs(1, False))