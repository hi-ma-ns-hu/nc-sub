class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = list()
        for i, v in enumerate(heights):
            l = i
            while stack and stack[-1][1] > v:
                idx, val = stack.pop()
                area = val * (l-idx)
                max_area = max(max_area, area)
                l = idx
            stack.append((l,v))
            
        for i, v in stack:
            max_area = max(max_area, v*(len(heights)-i))
        return max_area