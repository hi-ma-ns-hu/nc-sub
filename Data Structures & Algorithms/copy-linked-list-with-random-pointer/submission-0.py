"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old2new = dict()

        curr = head
        while curr:
            old2new[curr.val] = Node(curr.val, curr.next, curr.random)
            curr = curr.next
        
        prev = None
        while curr:
            copied = old2new[curr]
            copied.next = old2new[curr.next]