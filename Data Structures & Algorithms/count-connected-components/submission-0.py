class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = 0
        visited = set()
        # adjacency List
        adj_list = defaultdict(list)
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)
        
        def dfs(index, prev_val):
            if index in visited: return False

            visited.add(index)
            for i in adj_list[index]:
                if i == prev_val: continue
                dfs(i, index)

        for i in range(n):
            if i not in visited:
                dfs(i, -1)
                res += 1
        return res