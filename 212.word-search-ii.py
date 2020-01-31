#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#


# @lc code=start
class Solution:
    # trie: O(M * 4 * 3^(L - 1)) if we do not do trimming and O(N)
    # where M is the number of cells and L is the length of word and N is the number
    # of words in the input
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def backtrack(row, col, parent):
            letter = board[row][col]
            node = parent[letter]
            word = node.pop(WORD_KEY, None)
            if word:
                res.append(word)

            board[row][col] = '#'
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_x, new_y = row + dx, col + dy
                if 0 <= new_x < m and 0 <= new_y < n and board[new_x][new_y] in node:
                    backtrack(new_x, new_y, node)
            board[row][col] = letter

            if not node:
                parent.pop(letter)

        res = []
        if not board:
            return res
        m, n = len(board), len(board[0])

        WORD_KEY = '$'
        # build a trie
        trie = dict()
        for word in words:
            node = trie
            for letter in word:
                node = node.setdefault(letter, dict())
            node[WORD_KEY] = word

        for i in range(m):
            for j in range(n):
                if board[i][j] in trie:
                    backtrack(i, j, trie)
        return res
# @lc code=end
