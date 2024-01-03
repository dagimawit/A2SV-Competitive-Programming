class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        answer = []
        i,j =0,0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                answer.append(nums1[i])
                i +=1
                j+=1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        if len(answer) == 0:
            return -1  # Return -1 if there are no common elements
        else:
            answer.sort()
            return answer[0]
        
        
        
        
        
        
        
        
        
        
        


        