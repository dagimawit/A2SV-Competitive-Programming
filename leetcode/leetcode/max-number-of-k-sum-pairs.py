class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        if not nums:
            return
        start , end , result= 0 , len(nums)-1 , 0
        while(start < end):
            sum = nums[start] + nums[end]
            if k > sum:
                start+=1
            elif k < sum:
                end-=1
            else:
                start+=1 ; end-=1 ; result+=1
        return result