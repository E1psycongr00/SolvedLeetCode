class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        solved = False
        def solve(r, c):
            nonlocal solved
            
            if solved:
                return
            
            if r >= len(board):
                solved = True
                return
            
            if board[r][c] != '.':
                solve(r +(c + 1) // len(board[0]), (c+1) % len(board[0]))
            else:
                for num in range(1, 10):
                    if check(r, c, str(num)):
                        board[r][c] = str(num)
                        solve(r +(c + 1) // len(board[0]), (c+1) % len(board[0]))
                        if solved:
                            return
                        board[r][c] = '.'
        
        def check(r, c, num):
            for i in range(9):
                if board[i][c] == num:
                    return False
                if board[r][i] == num:
                    return False
                if board[3 * (r // 3) + (i // 3)][3 * (c // 3) + (i % 3)]  == num:
                    return False
            return True

        solve(0, 0)