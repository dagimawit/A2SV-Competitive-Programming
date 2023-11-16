class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        substring_count= {}
        N = len(s)
        result = []
        window = 10
        
        for i in range(N- window + 1):
            substring = s[i:i+window]
            if substring in substring_count:
                if substring_count[substring] ==1:
                    result.append(substring)
                substring_count[substring] +=1
            else:
                substring_count[substring] = 1
        return result
        
        