class Solution:
    def trap(self, height: List[int]) -> int:
        prefix, prefix_arr = 0, list()
        suffix, suffix_arr = 0, list()
        res = 0

        # prefix
        for i in range(len(height)):
            prefix = max(prefix, height[i])
            prefix_arr.append(prefix)

        # suffix
        for i in range(len(height)-1, -1, -1):
            suffix = max(suffix, height[i])
            suffix_arr.append(suffix)
            
        suffix_arr.reverse()

        for i in range(len(height)):
            res += min(prefix_arr[i], suffix_arr[i])-height[i]

        return res