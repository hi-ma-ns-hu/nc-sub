class Solution:
  def findTargetSumWays(self, nums: List[int], target: int) -> int:
    cache = dict()

    def dfs(idx, tar):
      if len(nums) == idx: return target == tar # will return True(1) or False(0)
      if (idx, tar) in cache: return cache[(idx, tar)]
      cache[(idx, tar)] = dfs(idx+1, tar+nums[idx])+dfs(idx+1, tar-nums[idx])
      return cache[(idx, tar)]
      
    # tar is current total till now
    return dfs(0, 0)