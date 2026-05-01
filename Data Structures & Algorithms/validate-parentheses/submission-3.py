class Solution:
    def isValid(self, s: str) -> bool:
        d = {')': '(', '}': '{', ']': '['}
        stack = []

        for i in s:
            if i in d:
                if stack or stack[-1] != d[i]:
                    return False
                stack.pop()
            else:
                stack.append(i)
        return len(stack) == 0