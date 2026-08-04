class Solution:
  def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
    adj_list = defaultdict(list)

    visited = set()
    def dfs(index, prev_val):
      if index not in visited: return True

      visited.add(index)
      for i in adj_list[index]:
        if i == prev_val:
          if dfs(i, prev_val): return True
      return False
    
    for a, b in edges:
      if a in adj_list and b in adj_list:
        if dfs(a, b): return [a, b] # builds adj list incrementally, before adding edges check if there already exists a path between two
      adj_list[a].append(b)
      adj_list[b].append(a)