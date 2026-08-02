class Solution:
  def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    courPreMap = defaultdict(list)
    for crs, pre in prerequisites:
      courPreMap[crs].append(pre)

    res = list()
    visited = set()

    def dfs(course):
      if course in visited: return False
      if courPreMap[course] == []:
        if course in res: return True

      visited.add(course)
      for pre in courPreMap[course]:
        if not dfs(pre): return False

      visited.remove(course)
      courPreMap[course] = []
      res.append(course)
      return True

    for course in range(numCourses):
      if not dfs(course): return list()
    return  res
