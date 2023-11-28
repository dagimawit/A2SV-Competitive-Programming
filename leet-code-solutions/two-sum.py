class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value_map = {}
        for i,num in enumerate(nums):
            if num in value_map:
                return [value_map[num],i]
            complment = target - num
            value_map[complment] = i
        return []
        