class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += f'{s}#'
        return res

    def decode(self, s: str) -> List[str]:
        st = s.split('#')
        res = list()
        for i in st[:-1]:
            res.append(i)
        return res