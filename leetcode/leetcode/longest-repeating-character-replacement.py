class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longeCount = {}
        result  = 0
        l = 0
        maximum_freq  =0
        
        for r in range(len(s)):
            longeCount[s[r]] = 1 + longeCount.get(s[r],0)
            maximum_freq = max(maximum_freq , longeCount[s[r]])
                
            
            while (r-l + 1) - maximum_freq > k:
                longeCount[s[l]] -=1
                l +=1
            
            result = max(result, r-l+1)
        return result