# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        arr = list()
        curr = head
        while curr:
            arr.append(curr)
            curr = curr.next
        
        idx = len(arr)-n
        
        if idx == 0:
            return head.next
        
        arr[idx-1].next = arr[idx].next
        return head