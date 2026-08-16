class Solution:
  def lengthOfLIS(self, nums: List[int]) -> int:
    cache = [nums[0]]
    
    from bisect import bisect_left
    
    lis = 1
    for i in range(1, len(nums)):
      if cache[-1] < nums[i]:
        cache.append(nums[i])
        lis += 1
        continue
      
      idx = bisect_left(cache, nums[i])
      cache[idx] = nums[i]
    
    return lis