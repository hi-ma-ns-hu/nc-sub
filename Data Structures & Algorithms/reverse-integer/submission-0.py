class Solution:
    def reverse(self, x: int) -> int:
        original = x
        res = int(str(abs(x))[::-1])

        if original < 0: return -1*res
        
        if res < -1*(1 << 31) or res > (1 << 31): return 0

        return res