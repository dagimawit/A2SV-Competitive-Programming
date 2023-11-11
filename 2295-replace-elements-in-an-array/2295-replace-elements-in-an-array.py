class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        index_map = {}
        for i, num in enumerate(nums):
            index_map[num] = i
        for operation in operations:
            num1, num2 = operation
            index_map[num2] = index_map[num1]
            nums[index_map[num1]] = num2

        return nums