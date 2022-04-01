class Solution:
    def numIslands(self, board: List[List[str]]) -> int:
        cnt = 0
        
        def dfs(y, x, num):
            if y < 0 or y >= len(board) or x < 0 or x >= len(board[0]):
                return
            if board[y][x] != num:
                return
            
            board[y][x] = '0'
            
            dfs(y+1, x, num)
            dfs(y-1, x, num)
            dfs(y, x+1, num)
            dfs(y, x-1, num)
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != "0":
                    dfs(i, j, board[i][j])
                    cnt += 1
                    
        return cnt
                    