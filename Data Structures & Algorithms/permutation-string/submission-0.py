class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len, s2_len = len(s1), len(s2)
        if len(s1) > len(s2):
            return False

        s1_count = [0]*26
        s2_count = [0]*26