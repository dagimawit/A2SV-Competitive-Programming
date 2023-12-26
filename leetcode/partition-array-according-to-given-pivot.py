class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        mins = []
        maxs = []
        pivots=[]

        for i in nums:
            if i < pivot:
                mins.append(i)
            elif i > pivot:
                maxs.append(i)
            else:
                pivots.append(i)
        
        return mins + pivots + maxs
       
                
#             9 5   2 10  12 14
# 9 5  10 10  12 14