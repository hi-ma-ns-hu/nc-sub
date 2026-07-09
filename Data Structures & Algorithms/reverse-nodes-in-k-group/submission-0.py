# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        arr = list()
        curr = head
        # add to list
        while curr:
            arr.append(curr)
            curr = curr.next

        for i in range(0, len(arr), k):
            # reverse if k groups can be formed
            if i+k <= len(arr):
                arr[i:i+k] = reversed(arr[i:i+k])

        # join the reversed nodes
        for i in range(len(arr)-1):
            arr[i].next = arr[i+1]

        arr[-1].next = None

        return arr[0]