class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split('/')
        print(path)
        for char in  path:
            if char == '' or char =='.'  :
                continue
            if char == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(char)
        return '/' + '/'.join(stack)
          
            
# #           
                
            
        