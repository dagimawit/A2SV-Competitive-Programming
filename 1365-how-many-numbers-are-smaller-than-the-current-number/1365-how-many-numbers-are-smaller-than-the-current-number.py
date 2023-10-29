class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        sorted_nums = sorted(nums)
        result = []
        for num in nums:
            result.append(sorted_nums.index(num))
        
        return result
