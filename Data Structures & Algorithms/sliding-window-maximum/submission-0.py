class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        i, j = 0, k-1
        res = list()
        while j < len(nums):
            sn = nums[i:j+1]
            res.append(max(sn))
            i += 1
            j += 1

        return res