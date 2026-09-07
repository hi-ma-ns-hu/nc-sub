class Solution:
    def checkValidString(self, s: str) -> bool:
        open = close = 0

        for c in s:
            if c == '(':
                open += 1
                close += 1

            elif c == ')':
                open -= 1
                close -= 1

            else:
                open += 1
                close -= 1

            if open < 0: return False

            close = max(close, 0)

        return close == 0
            