class Solution:
  def canPartition(self, nums: List[int]) -> bool:
    total = sum(nums)
    if total % 2 != 0: return False

    target = total // 2

    cache = [[-1]*(target+1) for _ in range(len(nums)+1)]


    def dfs(idx, target):
        if idx >= len(nums): return target == 0
        
        if target < 0: return False

        if cache[idx][target] != -1: return cache[idx][target]

        cache[idx][target] = dfs(idx+1, target) or dfs(idx+1, target-nums[idx])

        return cache[idx][target]

    return dfs(0, target)