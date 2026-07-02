# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        slow, fast = head.next, head.next.next
        while slow and fast:
            print(slow.val, fast.val)
            if slow.val == fast.val:
                return True
            if slow.val != fast.val:
                slow = slow.next
                fast = fast.next.next
        return False
        