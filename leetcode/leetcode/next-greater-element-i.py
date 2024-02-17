class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nextGreater = {}
        result  = []
        stack = []
        
        for char in nums2:
            while stack and stack[-1] < char:
                nextGreater[stack.pop()] = char
            stack.append(char)
        for char2 in nums1:
            result.append(nextGreater.get(char2, -1))
        return result
            