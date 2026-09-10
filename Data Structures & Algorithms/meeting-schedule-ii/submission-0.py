"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals: return 0

        intervals.sort(key=lambda x: x.start)

        res = [intervals[0]]
        
        for i in range(len(intervals[1:])):
            if intervals[i+1].start < intervals[i].end:
                res.append(intervals[i+1])
            else:
                res[-1] = intervals[i+1]

        return len(res)