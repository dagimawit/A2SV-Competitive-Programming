class Solution:
    def reverseWords(self, s: str) -> str:
        strin=list(map(str,s.split()))
        l = 0
        r = len(strin) - 1
        while l < r:
            strin[l] , strin[r] = strin[r], strin[l]
            r -=1
            l +=1
        result = " ".join(strin)
        return result
        