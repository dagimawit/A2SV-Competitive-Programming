class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # l = 0
        r = k
        the_sum = sum(nums[:k])
        max_average = the_sum
        for l in range(1,len(nums)-k+1):
            the_sum = the_sum - nums[l-1] + nums[l+k-1]
            print(the_sum)
            max_average = max(the_sum,max_average)
        return max_average/k
            
            