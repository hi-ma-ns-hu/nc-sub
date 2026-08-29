class CountSquares:

    def __init__(self):
        self.points = list()
        self.points_count = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points.append(point)
        self.points_count[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point

        for x, y in self.points:
            # determine if its a diagonal point, otherwise continue
            if abs(px-x) != abs(py-y) or x == px or y == py: continue
            # now since this is a diagonal point, other two points will be (px, y) and (x, py)
            res += self.points_count[(px, y)]*self.points_count[(x,py)]
        return res