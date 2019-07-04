#
# Given a 2D board and a word, find if the word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
#
# Example:
#
# board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
#
# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false.


class Solution:

    def exist_core(self, board, flag, i, j, word, count):
        m = len(board)
        n = len(board[0])
        if word[count] == board[i][j]:
            if len(word) == count + 1:
                return True
            flag[i][j] = True
            tttt = False
            if i < m - 1 and not flag[i + 1][j]:
                tttt = self.exist_core(board, flag, i + 1, j, word, count + 1)
            if tttt:
                return True

            if i > 0 and not flag[i - 1][j]:
                tttt = self.exist_core(board, flag, i - 1, j, word, count + 1)
            if tttt:
                return True

            if j < n - 1 and not flag[i][j + 1]:
                tttt = self.exist_core(board, flag, i, j + 1, word, count + 1)
            if tttt:
                return True

            if j > 0 and not flag[i][j - 1]:
                tttt = self.exist_core(board, flag, i, j - 1, word, count + 1)
            if tttt:
                return True
            flag[i][j] = False
            return False

        else:
            return False

    def exist(self, board, word):
        m = len(board)
        if m < 1:
            return False
        len_word = len(word)
        if len_word < 1:
            return True
        n = len(board[0])
        rst = False
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    flag = [[False for jj in range(n)] for ii in range(m)]
                    flag[i][j] = True
                    if self.exist_core(board, flag, i, j, word, 0):
                        rst = True
                        break
            if rst:
                break
        return rst


if __name__ == '__main__':
    a = Solution()
    rst = a.exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], "ABCESEEEFS")
    print(rst)
