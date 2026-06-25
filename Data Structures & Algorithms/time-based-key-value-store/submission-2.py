class TimeMap:

    def __init__(self):
        self.store = defaultdict(list) # {key: [(val, ts)]}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        vals = self.store[key]
        l, r = 0, len(vals)-1
        while l <= r:
            m = (l+r)//2
            val = vals[m][1]
            if val <= timestamp:
                l = m+1
            else:
                r = m-1

        return vals[r][0] if r >= 0 else ''
        