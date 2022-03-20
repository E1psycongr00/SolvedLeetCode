import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collectors;


class Solution {
    public int numIslands(char[][] grid) {
        int rows = grid.length;
        int cols = grid[0].length;

        int[][] dirs = new int[][]{{1,0}, {0, 1}, {-1, 0}, {0, -1}};
        UnionFind uf = new UnionFind(rows * cols);
        int cnt1 = 0;
        int cnt2 = 0;
        for (int y = 0; y < rows; y++) {
            for (int x = 0; x < cols; x++) {
                cnt1 += (grid[y][x] == '1' )? 1 : 0;
                for (int i = 0; i < 4; i++) {
                    int cy = y + dirs[i][0];
                    int cx = x + dirs[i][1];
                    if (cy >= 0 && cy < rows && cx >= 0 && cx < cols && grid[cy][cx] == '1' && grid[y][x] == '1') {
                        if(!uf.isConnected(y*cols+x, cy*cols+cx)) {
                            uf.union(y*cols+x, cy*cols+cx);
                            cnt2 -= 1;
                        }
                    }
                }
            }
        }
        return cnt1 + cnt2;
    }
}

class UnionFind {
    int[] parent;
    int[] rank;

    public UnionFind(int size) {
        parent = new int[size];
        rank = new int[size];
        for (int i = 0; i < parent.length; i++) {
            parent[i] = i;
        }
        Arrays.fill(rank, 1);
    }

    public int find(int x) {
        if(x != parent[x]) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    public void union(int x, int y) {
        x = find(x);
        y = find(y);
        if(x != y) {
            if(rank[x] > rank[y]) {
                parent[y] = x;
            } else if (rank[x] < rank[y]) {
                parent[x] = y;
            } else {
                parent[y] = x;
                rank[x] += 1;
            }
        }
    }

    public boolean isConnected(int x, int y) {
        return find(x) == find(y);
    }
}