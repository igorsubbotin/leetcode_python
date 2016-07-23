# Valid Sudoku - https://leetcode.com/problems/valid-sudoku/
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        print ord("1")-49
        s = []
        for _ in xrange(27):
            s.append([0] * 9)
        for i in xrange(9):
            for j in xrange(9):
                c = board[i][j]
                if c == ".":
                    continue
                n = ord(c)-49
                s[i][n] += 1
                if s[i][n] > 1:
                    return False
                s[9 + j][n] += 1
                if s[9 + j][n] > 1:
                    return False
                a = s[18 + (i / 3) * 3 + (j / 3)]
                a[n] += 1
                if a[n] > 1:
                    return False
        return True