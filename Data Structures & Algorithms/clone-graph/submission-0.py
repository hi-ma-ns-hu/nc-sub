"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        map = dict()

        def dfs(node):
            if node in map: return map[node]
            
            deep_copied_node = Node(node.val)
            map[node] = deep_copied_node
            for neighbor in node.neighbors:
                deep_copied_node.neighbors.append(dfs(neighbor))
            return deep_copied_node
        
        return dfs(node) if node else None