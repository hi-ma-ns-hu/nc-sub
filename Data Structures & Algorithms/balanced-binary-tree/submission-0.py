# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            # if no node, then the tree is auto balanced
            # so True for result and 0 for height which will be used further
            if not node: return [True, 0]

            left = dfs(node.left)
            right = dfs(node.right)
            height = max(left+right)+1

            if abs(right[1]-left[1]) <= 1:
                return [True, height]
            return [False, height]
            
        return dfs(root)[0]