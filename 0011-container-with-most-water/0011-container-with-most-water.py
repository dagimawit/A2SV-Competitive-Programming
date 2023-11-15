class Solution:
    def maxArea(self, height: List[int]) -> int:
        answer = 0
        left = 0
        N = len(height)
        right = N-1
        while right > left:
            min_height = min(height[left],height[right])
            width = right - left
            area = width * min_height
            answer = max(answer,area)
            
            if min_height == height[left]:
                left +=1
            else:
                right -=1
        return answer