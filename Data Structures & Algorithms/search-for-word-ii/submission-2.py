class TrieNode:
    def __init__(self):
        self.children = dict()
        self.end = False

    def add_word(self, word: str):
        curr = self
        for s in word:
            if s not in curr.children:
                curr.children[s] = TrieNode()
            curr = curr.children[s]
        curr.end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows, cols = len(board), len(board[0])
        res = list()
        root = TrieNode()

        for w in words:
            root.add_word(w)

        def dfs(r, c, curr_word, curr_node, subset):

            if r < 0 or c < 0 or r >= rows or c >= cols or (r,c) in subset or board[r][c] not in curr_node.children:
                return
            
            curr_word += board[r][c]
            curr_node = curr_node.children[board[r][c]]
            if curr_node.end:
                res.append(curr_word)
                curr_node.end = False

            subset.add((r,c))

            dfs(r+1, c, curr_word, curr_node, subset)
            dfs(r-1, c, curr_word, curr_node, subset)
            dfs(r, c+1, curr_word, curr_node, subset)
            dfs(r, c-1, curr_word, curr_node, subset)
            
            subset.remove((r,c))

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, '', root, set())

        return res