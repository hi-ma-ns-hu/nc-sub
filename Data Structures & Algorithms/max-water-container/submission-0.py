class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights)-1
        res = 0
        while i < j:
            print('i', i, 'j', j)
            area = (j-i)*min(heights[i], heights[j])
            res = max(res, area)
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return res
