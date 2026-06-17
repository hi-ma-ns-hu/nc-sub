class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        for i in range(len(heights)):
            max_area = max(min(heights[i:len(heights)+1])*(len(heights)-i), max_area)

        return max_area