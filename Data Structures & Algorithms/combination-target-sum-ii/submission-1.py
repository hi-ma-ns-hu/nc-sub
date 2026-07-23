class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        candidates.sort()
        def dfs(index, subset, total):
            if total == target:
                res.add(tuple(subset))
                return
            
            if index >= len(candidates) or total > target:
                return
            
            subset.append(candidates[index])

            # include
            dfs(index+1, subset, candidates[index]+total)

            # exclude
            subset.pop()
            dfs(index+1, subset, total)

        dfs(0, list(), 0)

        return [list(i) for i in res]