class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_idx = dict()
        for i, c in enumerate(s):
            last_idx[c] = i

        size = 0 # size of the window substring
        end = 0 # end index of the window substring
        res = list()

        for i, c in enumerate(s):
            size += 1
            end = max(end, last_idx[c])
            
            if i == end:
                res.append(size)
                size = 0
        return res