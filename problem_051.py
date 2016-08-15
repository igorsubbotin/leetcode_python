# N-Queens - https://leetcode.com/problems/n-queens/
from copy import copy
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        s = set()
        for i in xrange(n):
            for j in xrange(n):
                s.add((i, j))
        return [toResult(x) for x in solve([s, [], n], n, 0)]
        
def solve(matrix, q, i):
    if q == 0:
        return [matrix]
    s, queens, n = matrix
    if len(s) == 0:
        return []
    res = []
    a = []
    for j in xrange(n):
        t = (i, j)
        if t in s:
            a.append(t)
            s.remove(t)
    for i, j in a:
        m = copyMatrix(matrix)
        putQueen(m, i, j)
        res += solve(m, q - 1, i + 1)
    return res

def putQueen(matrix, i, j):
    s, q, n = matrix
    q.append((i, j))
    if len(s) == 0:
        return
    for dj in [-1, 0, 1]:
        ix = i + 1
        jx = j + dj
        while ix < n and jx >= 0 and jx < n:
            t = (ix, jx)
            if t in s:
                s.remove(t)
            ix += 1
            jx += dj

def copyMatrix(matrix):
    s, q, n = matrix
    return [copy(s), copy(q), n]
        
def toResult(matrix):
    s, q, n = matrix
    res = []
    qs = set(q)
    for i in xrange(n):
        row = ""
        for j in xrange(n):
            if (i, j) in qs:
                row += "Q"
            else:
                row += "."
        res.append(row)
    return res