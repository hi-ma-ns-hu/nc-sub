class Solution:
  def findTargetSumWays(self, nums: List[int], target: int) -> int:
    def dfs(idx, tar):
      if len(nums) == idx: return target == tar # will return True(1) or False(0)
      return dfs(idx+1, tar+nums[idx])+dfs(idx+1, tar-nums[idx])

    # tar is current total till now
    return dfs(0, 0)