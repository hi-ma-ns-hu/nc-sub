class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cache = dict()
        def dfs(idx):
            if idx in cache: return cache[idx]

            if idx == len(nums)-1: return True

            end = min(idx+nums[idx], len(nums)-1) # actually idx+min[idx] is the end but what if the index crosses len of nums
            for i in range(idx+1, end+1):
                if dfs(i):
                    cache[i] = True
                    return True
            cache[idx] = False
            return False
            
        return dfs(0)