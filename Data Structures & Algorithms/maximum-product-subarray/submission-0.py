class Solution:
  def maxProduct(self, nums: List[int]) -> int:
    res = 0
    for i in range(len(nums)-1):
      res = max(res, nums[i]*nums[i+1])
    return res