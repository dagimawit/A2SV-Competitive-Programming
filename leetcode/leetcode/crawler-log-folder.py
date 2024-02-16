class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        count = 0 
        for char in logs:
            if char == './':
                continue
            if char == '../':
                if stack:
                    stack.pop()
                    count -=1
            else:
                stack.append(char)
                count +=1
        return count
                
                
                
        
        