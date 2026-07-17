class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = list()
        heapq.heapify(heap)

        for point in points:
            distance = (point[0]*point[0]) + (point[1]*point[1])
            heapq.heappush(heap, (-distance, point))
            while len(heap) > k:
                heapq.heappop(heap)

        return [point[1] for point in heap]