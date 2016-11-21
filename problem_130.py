# Surrounded Regions - https://leetcode.com/problems/surrounded-regions/
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        n = len(board)
        if n == 0:
            return
        m = len(board[0])
        v = set()
        for x in xrange(n):
            for y in xrange(m):
                if not (x == 0 or x == n-1) and (y != 0 and y != m-1):
                    continue
                p = (x,y)
                if p not in v and board[x][y] == 'O':
                    v = v.union(getRegion(p, board))
        for x in xrange(n):
            for y in xrange(m):
                p = (x,y)
                if p not in v:
                    board[x][y] = 'X'
                
def getRegion(point, board):
    s = [point]
    i = 0
    v = set()
    while i < len(s):
        p = s[i]
        i += 1
        if p not in v:
            v.add(p)
            for np in getLegalMoves(p, board):
                if np not in v:
                    s.append(np)
    return v
        
def getLegalMoves(point, board):
    res = []
    x, y = point
    if x - 1 >= 0 and board[x-1][y] == 'O':
        res.append((x-1,y))
    if x + 1 < len(board) and board[x+1][y] == 'O':
        res.append((x+1,y))
    if y - 1 >= 0 and board[x][y-1] == 'O':
        res.append((x,y-1))
    if y + 1 < len(board[0]) and board[x][y+1] == 'O':
        res.append((x,y+1))
    return res