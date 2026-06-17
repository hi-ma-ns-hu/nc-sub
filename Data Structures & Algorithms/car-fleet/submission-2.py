class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = list()
        pair = sorted(list(zip(position, speed)), reverse=True)
        for p, s in pair:
            while not stack or  (stack and stack[-1] < ((target-p)/s)):
                stack.append((target-p)/s)
        return len(stack)