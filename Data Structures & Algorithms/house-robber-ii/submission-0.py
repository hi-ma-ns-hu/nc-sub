class Solution:
  def rob(self, nums: List[int]) -> int:
    def dfs(index, flag):
        if index >= len(nums) or (flag and index == len(nums)-1): return 0
        return max(dfs(index+2, flag or index == 0)+nums[index],dfs(index+1, flag))
    return max(dfs(0, True), dfs(1, False))      