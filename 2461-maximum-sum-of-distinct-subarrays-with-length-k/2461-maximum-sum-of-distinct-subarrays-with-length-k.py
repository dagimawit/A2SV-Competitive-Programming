class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        maxSum = 0
        maxsubarraySum = 0
        subarrayset = set()
        l = 0
        
        for r in range(len(nums)):
            while nums[r] in subarrayset or r -l >= k:
                maxsubarraySum -= nums[l]
                subarrayset.remove(nums[l])
                l +=1
            maxsubarraySum +=(nums[r])
            subarrayset.add(nums[r])
            
            if r-l + 1 ==k:
                maxSum = max( maxsubarraySum,maxSum)
        return maxSum
        
                