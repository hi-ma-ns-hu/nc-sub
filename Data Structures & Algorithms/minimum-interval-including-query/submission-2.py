class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:

        res = dict()
        heap = list()
        idx = 0 # index for intervals iteration
        
        intervals.sort(key=lambda x: x[0])
        for q in sorted(queries):
            # if start <= q push to heap
            while idx < len(intervals) and intervals[idx][0] <= q:
                s, e = intervals[idx]
                heapq.heappush(heap, (e-s+1, e))
                idx += 1

            # if end is less than q: pop from heap
            while heap and heap[0][1] < q:
                heapq.heappop(heap)

            res[q] = heap[0][0] if heap else -1

        return [res[q] for q in queries]