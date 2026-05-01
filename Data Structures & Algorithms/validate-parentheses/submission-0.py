class Solution:
    def isValid(self, s: str) -> bool:
        d = {')': '(', '}': '{', ']': '['}
        i, j = 0, len(s)-1
        while i < j:
            if s[i] != d[s[j]]:
                return False
            i += 1
            j -= 1
        return True