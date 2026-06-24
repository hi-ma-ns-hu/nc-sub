class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r # at max he will eat max(piles) bananas each hour
        while l <= r:
            m = (l+r)//2
            h_mid = 0
            for i in piles:
                h_mid += math.ceil(i/m)
            if h_mid <= h:
                res = min(res, m)
                r = m-1
            else:
                l = m+1
        return res