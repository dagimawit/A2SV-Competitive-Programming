class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l,r =0 , len(nums)-1
        while l < r:
            cSum = nums[l] + nums[r]
            if cSum > target :
                r -=1
            elif cSum < target:
                l +=1
            else:
                return [l+1,r+1]
        return [l+1,r+1]
        
        