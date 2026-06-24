class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        res = nums[0]
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            m = (l+r)//2
            # mid could also be potentially the small value then current res
            res = min(res, nums[m])
            if nums[l] <= nums[m]:
                # means left is sorted search right
                l = m+1
            else:
                # right is sorted search left
                r = m-1
        return res