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
                if item:
                    nested.append(item.val)
                    queue.append(item.left)
                    queue.append(item.right)

            if nested: res.append(nested)
        return res