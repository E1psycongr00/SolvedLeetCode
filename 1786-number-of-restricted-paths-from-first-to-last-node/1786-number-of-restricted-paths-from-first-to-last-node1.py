import collections
import heapq
from functools import lru_cache

class Solution:
    def countRestrictedPaths(self, n, edges):

        @lru_cache(maxsize=2 * (10**4))
        def path(u):
            if u == n:
                return 1
            ans = 0
            for v, w in g[u].items():
                if dis[v] >= dis[u]:
                    continue
                ans += path(v)
            return ans

        # 1, build graph
        g = [collections.defaultdict(lambda: float('inf')) for _ in range(n+1)]
        for u, v, w in edges:
            g[u][v] = w
            g[v][u] = w
			
        # 2. foreach node, find out the shortest path toward n
        dis = [float('inf') for _ in range(n+1)]
        g[n][n] = 0
        
		# (node, w)
        queue = [(0, n)]
        heapq.heapify(queue)
        while queue:
            d, u = heapq.heappop(queue)
            if dis[u]  != float('inf'):continue
            dis[u] = d
            for v, w in g[u].items():
			    # find the shortest path
                if dis[v] == float('inf'):
                    heapq.heappush(queue, (d+w, v))
        return path(1) % (10**9 + 7)
