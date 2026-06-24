class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l <= r:
            m = (l+r)//2
            h_m = 0
            for i in piles:
                h_m += math.ceil(i/m)
            if h_m <= h:
                return m
            else:
                l = m+1
