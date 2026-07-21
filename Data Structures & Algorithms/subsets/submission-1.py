class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = list()

        def dfs(index, subset):
            if index >= len(nums):
                res.append(subset[:])
                return
            
            subset.append(nums[index])
            # include
            dfs(index+1, subset)

            # exclude (means backtrack)
            subset.pop()
            dfs(index+1, subset)

        dfs(0, list())
        return res