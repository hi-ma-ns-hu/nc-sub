class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for i in nums:
            d[i] += 1

        heap = list()
        for i in d:
            heapq.heappush(heap, (d[i], i))
            if len(heap) > k:
                heapq.heappop(heap)
        return [i[1] for i in heap]