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
            if val == timestamp:
                return vals[m][0]
            elif val < timestamp:
                l = m+1
            else:
                r = m-1
        
        # if l and r have moved out of bounds or are at the last and first item respectively
        if l >= len(vals):
            return vals[r][0]
        if r <= 0:
            return vals[l][0]

        # find abs difference to the timestamp target
        abs_low = abs(vals[l][1]-timestamp)
        abs_high = abs(vals[r][1] - timestamp)

        return vals[l][0] if abs_low < abs_high else vals[r][0]

        