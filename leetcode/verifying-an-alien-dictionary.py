class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alphabet = {}
        for i, char in enumerate(order):
            alphabet[char] = i
    
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
        
            for j in range(min(len(word1), len(word2))):
                char1 = word1[j]
                char2 = word2[j]
            
                if char1 != char2:
                    if alphabet[char1] > alphabet[char2]:
                        return False
                    break
            else:
                if len(word1) > len(word2):
                    return False
        return True