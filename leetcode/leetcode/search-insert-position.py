class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)-1
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
            elif nums[n] < target:
                return  n +1
                