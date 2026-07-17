class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-i for i in stones]
        heapq.heapify(heap)
        while len(heap) >= 2:
            y = -heapq.heappop(heap)
            x = -heapq.heappop(heap)
            if x != y:
                diff = abs(y-x)
                heapq.heappush(heap, -diff)
        return -heap[0] if heap[0] else 0