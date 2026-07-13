# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSameTree(self, n1: Optional[TreeNode], n2: Optional[TreeNode]) -> bool:
        if not n1 and not n2: return True
        if not n1 or not n2 or n1.val != n2.val: return False

        left = self.isSameTree(n1.left, n2.left)
        right = self.isSameTree(n1.right, n2.right)
        return left and right

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root: return False
        if not subRoot: return True
        if self.isSameTree(root, subRoot): return True

        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)
        return left or right