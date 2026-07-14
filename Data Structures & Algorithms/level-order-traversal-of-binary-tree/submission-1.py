# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        queue = deque([root])
        res = list()

        while queue:
            nested = list()
            for _ in range(len(queue)):
                item = queue.popleft()
                nested.append(item.val)
                if item.left: queue.append(item.left)
                if item.right: queue.append(item.right)

            if nested: res.append(nested)
        return res