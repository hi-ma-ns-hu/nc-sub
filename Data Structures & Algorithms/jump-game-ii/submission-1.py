class Solution:
    def jump(self, nums: List[int]) -> int:
        cache = dict()
        def dfs(idx):
            if idx in cache: return cache[idx]
            if idx == len(nums)-1: return 0
            if nums[idx] == 0: return float('inf')

            end = min(len(nums)-1, idx+nums[idx])
            
            res = float('inf')
            for i in range(idx+1, end+1):
                res = min(res, 1+dfs(i))
            cache[idx] = res
            return res

        return dfs(0)