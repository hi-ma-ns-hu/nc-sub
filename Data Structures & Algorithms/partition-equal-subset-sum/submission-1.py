class Solution:
  def canPartition(self, nums: List[int]) -> bool:
    total = sum(nums)
    if total % 2 != 0: return False

    target = total // 2

    cache = [False]*(target+1) # dp is for target
    cache[0] = True # target 0 is alway achievable
    
    for num in nums:
        for tar in range(target, -1, -1):
            cache[tar] = cache[tar] or cache[tar-num]

    return cache[target]