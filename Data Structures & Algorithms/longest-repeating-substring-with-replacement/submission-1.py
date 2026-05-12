class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = 0
        freq = dict()
        mf = 0
        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0)+1
            mf = max(mf, freq[s[r]])
            while (r-l + 1)-mf > k:
                freq[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        return res