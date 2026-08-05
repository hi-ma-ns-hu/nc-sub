class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)

        def dfs(index, pre_val, visited):
            if index in visited: return False
            if index == pre_val: return True

            visited.add(index)
            for i in adj_list[index]:
                if dfs(i, pre_val, visited): return True
            return False

        for a, b in edges:
            if a in adj_list and b in adj_list:
                if dfs(a, b, set()): return [a, b]
            adj_list[a].append(b)
            adj_list[b].append(a)
        return []