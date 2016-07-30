# Sudoku Solver - https://leetcode.com/problems/sudoku-solver/
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.counter = 0
        a = []
        for i in xrange(9):
            a.append([])
            for j in xrange(9):
                a[i].append((-1, set(range(1, 10))))
        for i in xrange(9):
            for j in xrange(9):
                c = board[i][j]
                if c == ".":
                    continue
                self.updateItem(a, i, j, int(c))
        a = self.solve(a)
        for i in xrange(9):
            for j in xrange(9):
                board[i][j] = str(a[i][j][0])
                
    def solve(self, a):
        if self.counter == 81:
            return a
        while True:
            chk = []
            for i in xrange(9):
                for j in xrange(9):
                    n, s = a[i][j]
                    if n == -1:
                        chk.append((len(s), s, i, j))    
            chk.sort()
            for ln, s, i, j in chk:
                for x in s:
                    c = copyBoard(a)
                    cnt = self.counter
                    self.updateItem(c, i, j, x)
                    if self.counter == 81 and checkBoard(c):
                        return c
                    else:
                        self.counter = cnt

    def updateItem(self, a, i, j, n):
        if a[i][j][0] == -1:
            self.counter += 1
        else:
            return
        a[i][j] = (n, None)
        for m in xrange(3):
            for k in xrange(9):
                if m == 0:
                    ix = i
                    jx = k
                elif m == 1:
                    ix = k
                    jx = j
                else:
                    ix = (i / 3) * 3 + k % 3
                    jx = (j / 3) * 3 + k / 3
                nn, s = a[ix][jx]
                if nn == -1 and n in s:
                    s.remove(n)
                    if len(s) == 1:
                        self.updateItem(a, ix, jx, list(s)[0])
                    
def copyBoard(a):
    c = []
    for i in xrange(9):
        c.append([])
        for j in xrange(9):
            n, s = a[i][j]
            if n == -1:
                c[i].append((n, set(s)))
            else:
                c[i].append((n, None))
    return c

def checkBoard(board):
    a = []
    for _ in range(27):
        a.append([0] * 9)
    for i in range(9):
        for j in range(9):
            n, s = board[i][j]
            if n != -1:
                a[i][n - 1] += 1
                a[j + 9][n - 1] += 1
                a[18 + (i / 3) * 3 + (j / 3)][n - 1] += 1
    for i in range(27):
        for j in range(9):
            if a[i][j] > 1:
                return False
    return True