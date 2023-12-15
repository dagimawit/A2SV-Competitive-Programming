class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen_numbers = set()
        for num in nums:
            if num in seen_numbers:
                return num
            seen_numbers.add(num)
        return -1