class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1]+nums+[1]

        def dfs(nums):
            if len(nums) == 2: return 0 # because 2 ones are outer item

            max_coins = 0
            for i in range(1, len(nums)-1):
                curr_coins = nums[i-1]*nums[i]*nums[i+1]
                curr_coins += dfs(nums[:i] + nums[i+1:])
                max_coins = max(max_coins, curr_coins)
            return max_coins

        return dfs(nums)