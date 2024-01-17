class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        v="aeiou"
        mc=0
        c=0
        for i in s[0:k]:
            if i in v:
                c+=1
        mc=c        
        for i in range(k,len(s)):
            if s[i-k] in v:
                c-=1
            if s[i] in v:
                c+=1
            if mc<c:
                mc=c
        return mc