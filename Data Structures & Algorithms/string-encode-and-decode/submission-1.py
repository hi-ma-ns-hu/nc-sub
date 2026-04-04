class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += f'{len(s)}#{s}'
        return res

    def decode(self, s: str) -> List[str]:
        res = list()
        i = 0
        while i < len(s):
            left = i+2
            right = left + int(s[i])
            res.append(s[left:right])
            i = right
        return res