class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:

        res = dict()
        heap = list()
        
        intervals.sort(key=lambda x: x[0])
        for q in sorted(queries):
            for s, e in intervals:
                if s <= q: heapq.heappush(heap, (e-s+1, e))

            while heap and heap[0][1] < q:
                heapq.heappop(heap)

            res[q] = heap[0][0] if heap else -1

        return [res[q] for q in queries]