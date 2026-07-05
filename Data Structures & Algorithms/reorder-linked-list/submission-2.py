# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseLL(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

    def merge_node(self, head: Optional[ListNode], head3: Optional[ListNode]) -> Optional[ListNode]:
        while head and head3:
            nxt1 = head.next
            nxt3 = head3.next
            # prev.next = head
            head.next = head3
            head3.next = nxt1

            head = nxt1
            head3 = nxt3

    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return

        # get midpoint
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        head2 = slow.next
        slow.next = None

        # reverse the second nodelist
        # head3 is reversed head
        head3 = self.reverseLL(head2)
        
        # merge head and head3
        self.merge_node(head, head3)
