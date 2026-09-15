class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)

        for s, d, p in flights:
            adj[s].append((p, d))

        heap = [(0, src, 0)] # price, dest, stops (no of stops which we took to reach des from src); starting out we paid 0 to reach src node with 0 stops
        dist = [[float('inf')]*(k+2) for _ in range(n)]
        dist[src][0] = 0
        while heap:
            price, dest, stops = heapq.heappop(heap)

            if dest == dst: return price

            if stops > k: continue

            for new_price, new_dest in adj[dest]:
                np = new_price+price
                ns = stops+1

                if np < dist[new_dest][ns]:
                    dist[new_dest][ns] = np
                    heapq.heappush(heap, (np, new_dest, ns))

        return -1