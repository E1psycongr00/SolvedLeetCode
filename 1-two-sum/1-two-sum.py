class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Map = {}
        for i, num in enumerate(nums):
            Map[num] = i
        
        for i, num in enumerate(nums):
            if target - num in Map and i != Map[target - num]:
                return [i, Map[target-num]]