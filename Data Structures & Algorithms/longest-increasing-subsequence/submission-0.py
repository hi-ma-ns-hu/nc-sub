class Solution:
  def lengthOfLIS(self, nums: List[int]) -> int:
    cache = [-1]*len(nums)
    def dfs(index):
      if cache[index] != -1: return cache[index]

      lis = 1 # default 1, because the num is always a subsequence

      for j in range(index+1, len(nums)):
        if nums[j] > nums[index]:
          lis = max(lis, 1+dfs(j))
      
      cache[index] = lis
      return lis

    return max(dfs(i) for i in range(len(nums))) # we're checking for each of the i in num, what is the longest subsequence