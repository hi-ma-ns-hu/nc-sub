class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        res = 0
        heap = [(k, 0)] # kth node and 0 time for starting node
        visited = set()

        neigh = defaultdict(list)
        for u, v, w in times:
            neigh[u].append((v, w)) # node and time a neighbour is associated with

        while heap:
            node, time = heapq.heappop(heap)

            if node in visited: continue

            visited.add(node)

            res = max(res, time)

            for n, t in neigh[node]:
                if n not in visited:
                    heapq.heappush(heap, (n, t+time))

        return res if len(visited) == n else -1