# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(root):
            if not root: return 0
            nonlocal res

            left = dfs(root.left)
            right = dfs(root.right)
            left_max = max(left, 0)
            right_max = max(right, 0)
            total = left_max + right_max + root.val
            res = max(res, total)
            return max(left_max, right_max)+root.val
        dfs(root)
        return res