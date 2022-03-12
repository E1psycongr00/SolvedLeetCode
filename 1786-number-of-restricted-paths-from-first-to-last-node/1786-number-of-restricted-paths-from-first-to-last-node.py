from collections import defaultdict
from heapq import *
from functools import lru_cache
import sys

class Solution:
    def getRestrictedPath(self, source, n ,G):
        # Dijstra
        INF = sys.maxsize
        dist = [INF] * (n+1)
        minHeap = [(0, source)]
        while minHeap:
            cost, node = heappop(minHeap)
            if dist[node] != INF : continue
            dist[node] = cost
            for nextCost, nextNode in G[node]:
                if dist[nextNode] == INF:
                    alt = (cost + nextCost)
                    heappush(minHeap, (cost+nextCost, nextNode))
        return dist
    
    
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:     
        @lru_cache(maxsize=2 * (10**4))
        def dfs(node):
            if node == n:
                return 1
            ret = 0
            for _, nextNode in G[node]:
                if dist[node] > dist[nextNode]:
                    ret += dfs(nextNode)
            return ret
        
        G = defaultdict(list)
        
        for u, v, w in edges:
            G[u].append((w,v))
            G[v].append((w,u))
        
        dist = self.getRestrictedPath(n, n, G)
        ret = dfs(1) % (10**9 + 7)
        return ret