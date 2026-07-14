# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return list()
        
        queue = deque([root])
        res = list()

        while queue:
            res.append(queue[-1].val)
            for _ in range(len(queue)):
                item = queue.popleft()
                if item.left: queue.append(item.left)
                if item.right: queue.append(item.right)

        return res
