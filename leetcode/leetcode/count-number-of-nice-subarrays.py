from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def at_most_k(nums, k):
            count = odd_count = result = left = 0
            for right in range(len(nums)):
                if nums[right] % 2 != 0:
                    odd_count += 1
                while odd_count > k:
                    if nums[left] % 2 != 0:
                        odd_count -= 1
                    left += 1
                count += right - left + 1
            return count
        
        return at_most_k(nums, k) - at_most_k(nums, k - 1)
