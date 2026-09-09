class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        left, right = 0, len(intervals)-1
        while left <= right:
            mid = (left+right)//2
            if intervals[mid][0] < newInterval[0]:
                left = mid+1
            else:
                right = mid-1

        intervals.insert(left, newInterval)
        
        res = list()
        for interval in intervals:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])

        return res
        