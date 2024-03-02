class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for char in s:
            if char == '(' or not stack or (stack and stack[-1] != '('):
                stack.append(char)
            else:
                stack.pop()
        return len(stack)