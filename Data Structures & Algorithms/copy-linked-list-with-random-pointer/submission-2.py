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
            old2new[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            copied = old2new[curr]
            copied.next = old2new.get(curr.next)
            copied.random = old2new.get(curr.random)
            curr = curr.next

        return old2new.get(head)