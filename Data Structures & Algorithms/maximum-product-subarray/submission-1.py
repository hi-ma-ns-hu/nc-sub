class Solution:
  def maxProduct(self, nums: List[int]) -> int:
    res = max(nums)
    curr_min, curr_max = 1, 1 # we're maintaining both because of possibility of working with -ve numbers
    for num in nums:
      if num == 0:
        curr_min, curr_max = 1, 1 # reset the curr_max and curr_min beuase 0 essentially divides nums array in two parts
        continue

      curr_max = max(num*curr_max, num*curr_min, num)
      curr_min = min(num*curr_max, num*curr_min, num)
      res = max(res, curr_max)
    return res