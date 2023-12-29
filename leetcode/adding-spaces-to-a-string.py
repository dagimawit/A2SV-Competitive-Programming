class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        s= list(s)
        result= []
        index = 0
        spaceindex = 0
        while(index < len(s)):
            if spaceindex < len(spaces) and index ==spaces[spaceindex]:
                result.append(' ')
                spaceindex +=1
            result.append(s[index])
            index +=1
        return ''.join(result) 
        