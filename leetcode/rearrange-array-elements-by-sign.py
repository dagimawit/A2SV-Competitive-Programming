class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        result = []
        nresult = []
        answer = []
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(nums[i])
            else: 
                nresult.append(nums[i])
        for val, vall in zip(result, nresult):
            answer.extend([val, vall])
        return answer

        