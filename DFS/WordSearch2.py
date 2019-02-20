"""
Lintcode:
https://www.lintcode.com/problem/word-search-ii/description
"""

class Solution:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
    """

    def wordSearchII(self, board, words):
        # write your code here

        # Store the words and their prefix in two sets to
        # facilitate the lookup
        # Space: O(n * L)
        word_set = set(words)
        # Space: O(n * L^2)
        prefix_set = set()
        for word in words:
            for i in range(len(word)):
                prefix_set.add(word[:i + 1])

        ans = set()
        visited = [[0] * len(board[0]) for _ in range(len(board))]
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] in prefix_set:
                    visited[r][c] = 1
                    self.dfs(board, r, c, board[r][c], visited, prefix_set, word_set, ans)
                    visited[r][c] = 0
        return list(ans)

    def dfs(self, board, x, y, prefix, visited, prefix_set, word_set, ans):
        """
        Backtracking dfs to find all the words beginning with prefix and go from (x, y)
        :param board:       original search board
        :param x:           current x location
        :param y:           current y location
        :param prefix:      all characters traversed before
        :param visited:     record visited locations
        :param prefix_set:  prefix_set of the words
        :param word_set:    set of words
        :param ans:         all words traversed in board that are in words
        :return:
        """
        if prefix not in prefix_set:
            return
        if prefix in word_set:
            ans.add(prefix)

        neighbors = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        for dx, dy in neighbors:
            x_, y_ = x + dx, y + dy
            if not self.in_board(board, x_, y_):
                continue
            if visited[x_][y_]:
                continue
            visited[x_][y_] = 1
            self.dfs(board,
                     x_,
                     y_,
                     prefix + board[x_][y_],
                     visited,
                     prefix_set,
                     word_set,
                     ans)
            visited[x_][y_] = 0

    def in_board(self, board, x, y):
        return 0 <= x < len(board) and 0 <= y < len(board[0])

