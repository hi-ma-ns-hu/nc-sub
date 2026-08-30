class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        for i in range(32):
            res += 1 if n&1 else 0
            n >>= 1
        return res