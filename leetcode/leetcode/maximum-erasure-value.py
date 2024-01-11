class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        cur_sum = 0
        maximum_sum = 0
        l = 0
        val = Counter() 
        for r  in range(len(nums)):
            cur_sum += nums[r]
            val[nums[r]] += 1
            
            while val[nums[r]] >1:
                cur_sum -=nums[l]
                val[nums[l]] -=1
                l +=1
            maximum_sum = max(cur_sum,maximum_sum)
        return maximum_sum
                

            
            
                       
            
        
        
        
        
        
        
        
        
#         cur_sum = 0
#         # max_sum  = float('-inf')
#         newnum = set()
#         for i in nums:
#             newnum.add(i)
#         for j in newnum:
#             cur_sum += j
#         return cur_sum
#         # return 0 if cur_sum == float('-inf') else cur_sum  1 1 1 2 2 2 1 1 1 3 