class UnionFind:
    parent = []
    rank = []
    virtualNode: int
    
    def __init__(self, rows, cols):
        self.parent = [i for i in range(rows * cols + 1)]
        self.rank = [1 for _ in range(rows * cols + 1)]
        self.virtualNode = rows * cols
    
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def merge(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if self.rank[x] > self.rank[y]:
                self.parent[y] = x
            elif self.rank[x] < self.rank[y]:
                self.parent[x] = y
            else:
                self.parent[y] = x
                self.rank[x] += 1
    
    def isConnected(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def solve(self, board) -> None:
        rows, cols = len(board), len(board[0])
        uf = UnionFind(rows, cols)
        
        def index(cols, y, x):
            return y * cols + x
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and (r in [0, rows - 1] or c in [0, cols - 1]):
                    uf.merge(uf.virtualNode, index(cols, r, c))
                
                elif board[r][c] == 'O':
                    curNode = index(cols, r, c)
                    if r + 1 < rows and board[r + 1][c] == 'O': uf.merge(curNode, index(cols, r + 1, c))
                    if r - 1 >= 0 and board[r - 1][c] == 'O': uf.merge(curNode, index(cols, r - 1, c))
                    if c + 1 < cols and board[r][c + 1] == 'O': uf.merge(curNode, index(cols, r, c + 1))
                    if c - 1 >= 0 and board[r][c - 1] == 'O': uf.merge(curNode, index(cols, r, c - 1))
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O' and not uf.isConnected(index(cols, i, j), uf.virtualNode):
                    board[i][j] = 'X'
