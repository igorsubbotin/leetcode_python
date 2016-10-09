# Word Search - https://leetcode.com/problems/word-search/
from copy import copy
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if board[i][j] == word[0]:
                    s = []
                    v = set()
                    v.add((i, j))
                    s.append((i, j, 0, v))
                    while len(s) > 0:
                        ix, jx, k, v = s.pop()
                        v.add((ix, jx))
                        k += 1
                        if k == len(word):
                            return True
                        for iy, jy in getLegalMoves(ix, jx, board, v, word[k]):
                            s.append((iy, jy, k, copy(v)))
        return False
    
def getLegalMoves(i, j, board, v, c):
    res = []
    if isLegalMove(i + 1, j, board, v, c):
        res.append((i + 1, j))
    if isLegalMove(i - 1, j, board, v, c):
        res.append((i - 1, j))
    if isLegalMove(i, j + 1, board, v, c):
        res.append((i, j + 1))
    if isLegalMove(i, j - 1, board, v, c):
        res.append((i, j - 1))
    return res

def isLegalMove(i, j, board, v, c):
    if (i, j) in v:
        return False
    if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
        return False
    if board[i][j] != c:
        return False
    return True