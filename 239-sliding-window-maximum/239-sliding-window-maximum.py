from heapq import *

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        result = []
        for idx, num in enumerate(nums):
            heappush(heap, (-num, idx))
            if idx < k-1:
                continue
            while heap and heap[0][1] < idx - k +1:
                heappop(heap)
            if heap:
                result.append(-heap[0][0])
        return result