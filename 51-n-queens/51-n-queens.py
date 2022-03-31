class Solution:
    def solveNQueens(self, n: int):
        board = [['.'] * n  for _ in range(n)]
        result = []
        
        def solve(r):
            if r >= n - 1:
                result.append(makeString(board))
                return
            for i in range(n):
                if check(r+1, i):
                    board[r+1][i] = 'Q'
                    solve(r+1)
                    board[r+1][i] = '.'
        
        def check(row, col):
            for i in range(row):
                for j in range(n):
                    if board[i][j] == 'Q':
                        if col == j: return False
                        if col == j - (row - i): return False
                        if col == j + (row - i): return False
            return True
        
        def makeString(board):
            res = []
            for b in board:
                res.append(''.join(b))
            return res
        
        solve(-1)
        return result