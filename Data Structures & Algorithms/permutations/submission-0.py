class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = list()
        def dfs(index):            
            if index == len(nums):
                res.append(nums[:])
                return

            for i in range(index, len(nums)):
                # swap because this is what we need here to explore other positions
                nums[index], nums[i] = nums[i], nums[index]

                dfs(index+1)

                # backtrack, by reversing the above swap
                nums[index], nums[i] = nums[i], nums[index]

        dfs(0)
        return res