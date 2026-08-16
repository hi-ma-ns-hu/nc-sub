class Solution:
  def maxProduct(self, nums: List[int]) -> int:
    res = max(nums)
    curr_min, curr_max = nums[0], nums[0] # we're maintaining both because of possibility of working with -ve numbers
    for num in nums[1:]:
      # 

      temp = num*curr_max
      curr_max = max(temp, num*curr_min, num)
      curr_min = min(temp, num*curr_min, num)
      res = max(res, curr_max)
    return res