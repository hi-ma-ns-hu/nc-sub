class Solution:
    def canJump(self, nums: List[int]) -> bool:
        res = 0
        for i in range(len(nums)):
            if i > res: return False
            res = max(res, i+nums[i])
        return True