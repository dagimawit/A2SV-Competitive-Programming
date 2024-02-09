class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        freelem = 0
        for i, num in enumerate(nums):
            if num != val:
                nums[freelem] = num
                freelem +=1
        return freelem
                
   
#       2 2 
#           3 2 2 3  valueto be removed is 3
