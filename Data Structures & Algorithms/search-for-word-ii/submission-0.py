class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[0])
        res, trie = set(), {}
        for word in words:
            node = trie
            for c in word:
                node = node.setdefault(c, {})
            node['word'] = word

        def backtrack(r, c, node):
            if 'word' in node:
                res.add(node['word'])
            tmp, board[r][c] = board[r][c], '*'
            for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr, nc = r + dr, c + dc
                if (0 <= nr < ROWS and 0 <= nc < COLS and 
                    board[nr][nc] in node):
                    backtrack(nr, nc, node[board[nr][nc]])
            board[r][c] = tmp

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] in trie:
                    backtrack(r, c, trie[board[r][c]])
        return list(res)