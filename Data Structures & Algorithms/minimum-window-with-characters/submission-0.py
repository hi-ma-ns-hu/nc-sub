class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need, missing = Counter(t), len(t)
        l, start = 0, 0
        min_length = float('inf')

        for r in range(len(s)):
            char = s[r]

            if char in need:
                need[char] -= 1
                # subtract from missing only if need[char] > 0
                # in case of extra char no need to do, because our condition is satisfied anyway
                if need[char] >= 0:
                    missing -= 1

            # all missing found
            while missing == 0:
                # if current window length is less than min_length, update the start with l
                if (r-l+1) < min_length:
                    min_length = r-l+1
                    start = l
                
                # undoing changes, when s[r] encountered it subtracted since we are now moving l
                # forward, we have to compensate that change
                if s[l] in need:
                    need[s[l]] += 1

                    # and after compensating if the need[s[l]] increase to more than zero,
                    # we have to increase the missing too
                    if need[s[l]] > 0:
                        missing += 1

                l += 1

        return '' if min_length == float('inf') else s[start: start+min_length]