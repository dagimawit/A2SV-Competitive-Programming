class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        result = []
        repeated = {}
        n =len(nums)
        for i in range(len(nums)):
            if nums[i] in repeated:
                count = repeated[nums[i]]
            else:
                count = 0
            count +=1
            repeated[nums[i]] = count
        for key,value in repeated.items():
            if value > (n//3):
                result.append(key)
        return result
  