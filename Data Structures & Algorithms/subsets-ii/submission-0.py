class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = list()
        nums.sort()
        def dfs(index, subset):
            if index >= len(nums):
                res.append(subset[:])
                return
            
            subset.append(nums[index])
            # include
            dfs(index+1, subset)
            # backtrack
            subset.pop()
            # exclude
            while (index+1) < len(nums) and nums[index] == nums[index+1]:
                index += 1
            dfs(index+1, subset)
            
        dfs(0, [])
        return res
        