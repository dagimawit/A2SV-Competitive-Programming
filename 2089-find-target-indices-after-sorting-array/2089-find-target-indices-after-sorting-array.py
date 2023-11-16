class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        N =len(nums)
        result = []
        for i in range(N):
            if nums[i] ==target:
                result.append(i)
        return result if result else []
        