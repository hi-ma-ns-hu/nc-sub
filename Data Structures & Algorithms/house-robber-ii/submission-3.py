class Solution:
  def rob(self, nums: List[int]) -> int:

    if not nums: return 0
    if len(nums) == 1: return nums[0]
    return max(self.helper(nums[:-1]), self.helper(nums[1:]))
  
  def helper(self, nums):
    memo = [0]*len(nums)

    if not nums: return 0
    if len(nums) == 1: return nums[0]

    memo[0], memo[1] = nums[0], max(nums[0], nums[1])

    for i in range(2, len(nums)):
        memo[i] = max(memo[i-1], memo[i-2]+nums[i])
    return memo[-1]