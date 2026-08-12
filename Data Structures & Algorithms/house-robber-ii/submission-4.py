class Solution:
  def rob(self, nums: List[int]) -> int:

    if not nums: return 0
    if len(nums) == 1: return nums[0]
    return max(self.helper(nums[:-1]), self.helper(nums[1:]))
  
  def helper(self, nums):
    a, b = 0, 0
    for num in nums:
        temp = max(a+num, b)
        a = b
        b = temp
    return b