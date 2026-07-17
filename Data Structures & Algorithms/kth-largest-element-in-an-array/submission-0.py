class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-i for i in nums]
        heapq.heapify(heap)
        res = 0
        for i in range(k):
            if i+1 == k:
                res = -heap[0]
                break
            heapq.heappop(heap)
        return res 