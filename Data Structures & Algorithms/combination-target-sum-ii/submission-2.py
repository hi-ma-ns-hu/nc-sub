class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = list()
        candidates.sort()
        def dfs(index, subset, total):
            if total == target:
                res.append(subset[:])
                return
            
            if index >= len(candidates) or total > target:
                return
            
            subset.append(candidates[index])

            # include
            dfs(index+1, subset, candidates[index]+total)

            subset.pop()
            # exclude
            while (index + 1) < len(candidates) and candidates[index] == candidates[index+1]:
                index += 1
            dfs(index+1, subset, total)

        dfs(0, list(), 0)

        return res