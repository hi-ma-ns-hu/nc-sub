class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = list()
        def dfs(index, subset, total):
            # base case
            # if total == target, result found
            if total == target:
                res.append(subset[:])
                return

            # if current index is out of bound or total > target, no need to explore further
            if index >= len(nums) or total > target:
                return

            subset.append(nums[index])

            # include with current index because duplicates are allowed
            dfs(index, subset, total+nums[index])

            # backtrack and now we can explore other paths
            subset.pop()
            dfs(index+1, subset, total)

        dfs(0, list(), 0) # args are index, subset, current total
        return res