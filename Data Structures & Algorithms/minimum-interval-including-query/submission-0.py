class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        res = list()
        for q in queries:
            curr = -1
            for s, e in intervals:
                if s <= q <= e:
                    if curr == -1 or curr > (e-s+1):
                        curr = e-s+1
            res.append(curr)
        return res