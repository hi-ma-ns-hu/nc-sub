class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        adj_list = defaultdict(list)
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)

        visited = set()
        def dfs(index, prev_val):
            if index in visited: return False

            visited.add(index)
            for i in adj_list[index]:
                if i == prev_val: continue # we are going to search for teh visited val, so skip

                if not dfs(i, index): return False
            return True                

        return dfs(0, -1) and n == len(visited)