class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        adj = defaultdict(list)

        for src, dest in sorted(tickets)[::-1]: # sorting for lexographically and reversing because because thins would push the items in desc order in array which in pop would give lowest order item to push to result for lexographically sorted result
            adj[src].append(dest)

        res = list()
        
        def dfs(src):
            # dfs until there is adj[src], if there is no adj[src] you've reached the end for that src, and append to the res
            while adj[src]:
                popped = adj[src].pop() # this would give smallest item from the adj list
                dfs(popped)
            res.append(src)

        dfs('JFK')
        return res[::-1]