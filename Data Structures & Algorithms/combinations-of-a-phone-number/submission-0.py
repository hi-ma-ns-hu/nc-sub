class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        res = list()
        
        def dfs(index, curr_str):
            # always len(digits) == len(curr_str) for base case, because its the same number of combinations
            if len(curr_str) == len(digits):
                res.append(curr_str)
                return

            for s in map[digits[index]]:
                dfs(index+1, curr_str+s)

        if digits:
            dfs(0, '')

        return res