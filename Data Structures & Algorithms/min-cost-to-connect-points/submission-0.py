class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        res = 0

        adj = defaultdict(list) # {node1: [(dist, node2), (dist, node3), ...]}
        
        for i in range(n):
            xi, yi = points[i]
            for j in range(i+1, n):
                xj, yj = points[j]
                dist = abs(xj-xi)+abs(yj-yi)
                adj[i].append((dist, j))
                adj[j].append((dist, i))

        
        heap = [(0, 0)] # distance with itself will be 0 for any given node
        visited = set()

        while len(visited) < n:
            dist, node = heapq.heappop(heap)

            if node in visited: continue

            res += dist
            visited.add(node)

            for nei_dist, nei_node in adj[node]:
                if nei_node not in visited: heapq.heappush(heap, (nei_dist, nei_node))

        return res