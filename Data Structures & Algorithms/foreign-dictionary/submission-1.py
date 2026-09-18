class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        adj = {ch: set() for w in words for ch in w}
        
        for i in range(len(words)-1):
            min_len = min(len(words[i]), len(words[i+1]))
            if len(words[i]) > len(words[i+1]) and words[i][:min_len] == words[i+1][:min_len]: return ''
            for j in range(min_len):
                if words[i][j] != words[i+1][j]:
                    adj[words[i][j]].add(words[i+1][j])
                    break

        res = list()
        visited = dict()

        def dfs(char):
            if char in visited: return visited[char]

            visited[char] = True

            for c in adj[char]:
                if dfs(c): return True
            
            visited[char]=False
            res.append(char)

        
        for ch in adj:
            if dfs(ch): return ''

        res.reverse()
        return ''.join(res)