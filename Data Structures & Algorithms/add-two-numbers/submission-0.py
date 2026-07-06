# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        p1, p2 = l1, l2
        carry = 0

        while p1 or p2:
            p1_val = p1.val if p1 else 0
            p2_val = p2.val if p2 else 0
            total = p1_val + p2_val + carry

            carry = total // 10
            
            curr.next = ListNode(total % 10)
            curr = curr.next

            p1 = p1.next
            p2 = p2.next
        
        if carry:
            curr.next = ListNode(carry)
        
        return dummy.next