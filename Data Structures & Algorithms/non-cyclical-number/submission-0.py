class Solution:
    def sum_of_squares(self, n: int) -> int:
        res = 0
        while n:
            digit = n % 10
            res += (digit**2)
            n = n // 10
        return res

    def isHappy(self, n: int) -> bool:
        visited = set()

        while n not in visited:
            visited.add(n)
            n = self.sum_of_squares(n)
            if n == 1: return True
        return False