from typing import List
class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        n = len(nums)
        count =0
        for i in range(n):
            j = i+1
            while j < n:
                if nums[i] + nums[j] < target:
                    count += 1
                j += 1
        return count
                
            
        