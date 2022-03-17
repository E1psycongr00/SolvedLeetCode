from collections import defaultdict
from heapq import *


class Solution:
	def dijstra(self, source, graph):
		minHeap = [(0, source)]
		visitDist = defaultdict(int)
		while minHeap:
			cost, node = heappop(minHeap)

			if node in visitDist:
				continue
			visitDist[node] = cost
			for nextCost, nextNode in graph[node]:
				if nextNode not in visitDist:
					nextDist = cost + nextCost
					heappush(minHeap, (nextDist, nextNode))

		return visitDist

	def countPaths(self, n: int, roads) -> int:
		def dp(node):
			if node == 0:
				return 1
			if node in history:
				return history[node]
			cnt = 0
			for nextCost, nextNode in G[node]:
				if nextNode in dist and dist[nextNode] + nextCost == dist[node]:
					cnt += dp(nextNode)
			history[node] = cnt
			return cnt

		history = {}
		# make Graph
		G = defaultdict(list)
		for a,b,c in roads:
			G[a].append((c, b))
			G[b].append((c, a))

		dist =  self.dijstra(0, G)
		result = dp(n-1) % (10 **9 + 7)
		return result