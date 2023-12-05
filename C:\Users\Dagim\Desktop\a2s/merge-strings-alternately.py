class Solution(object):
    def mergeAlternately(self, word1, word2):
        result = ""
        if len(word1) > len(word2):
            for d1,d2 in zip(word1,word2):
                result += d1+ d2
            result += word1[len(word2):]
        elif len(word2) > len(word1):
            for d1,d2 in zip(word1,word2):
                result += d1+d2
            result += word2[len(word1):]
        else:
            for d1,d2 in zip(word1, word2):
                result += d1 + d2
        return result
        