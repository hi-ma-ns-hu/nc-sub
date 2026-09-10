"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        intervals.sort(key=lambda x: x.start)

        heap = [] # min heap storing end time
        
        for interval in intervals:
            # if end <= start time, then we can reuse that interval, so pop from the heap
            if heap and heap[0] <= interval.start:
                heapq.heappop(heap)
            
            # push current meeting end time
            heapq.heappush(heap, interval.end)


        return len(heap)