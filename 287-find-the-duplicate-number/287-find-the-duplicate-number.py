from collections import Counter

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        counter = Counter(nums)
        for i, c in counter.items():
            if c > 1:
                return i