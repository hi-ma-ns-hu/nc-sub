class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len, s2_len = len(s1), len(s2)

        if s1_len > s2_len:
            return False

        s1_count = [0]*26
        s2_count = [0]*26

        for i in range(s1_len):
            s1_count[ord(s1[i])-ord('a')] += 1
            s2_count[ord(s2[i])-ord('a')] += 1

        if s1_count == s2_count:
            return True

        for i in range(s1_len, s2_len):
            lc = ord(s2[i-s1_len])-ord('a')
            rc = ord(s2[i])-ord('a')

            s2_count[lc] -= 1
            s2_count[rc] += 1

            if s1_count == s2_count:
                return True
                
        return False
