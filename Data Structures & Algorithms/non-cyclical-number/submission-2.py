class Solution:
    def sum_of_squares(self, n: int) -> int:
        res = 0
        while n:
            digit = n % 10
            res += (digit**2)
            n = n // 10
        return res

    def isHappy(self, n: int) -> bool:
        slow, fast = n, self.sum_of_squares(n)

        while slow != fast:
            fast = self.sum_of_squares(self.sum_of_squares(fast))
            slow = self.sum_of_squares(slow)
        
        return True if fast == 1 else False