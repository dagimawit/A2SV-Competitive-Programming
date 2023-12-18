class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        window_size = 0
        max_window_size = 0
        for num in nums:
            if num == 1:
                window_size +=1
                max_window_size = max(window_size,max_window_size)
            else:
                window_size = 0
        return max_window_size
            
        