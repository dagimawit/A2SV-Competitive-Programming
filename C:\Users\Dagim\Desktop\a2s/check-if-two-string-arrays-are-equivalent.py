class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        list_str1 = ''.join(word1)
        list_str2 = ''.join(word2)
        if str(list_str1) == str(list_str2):
            return True
        return False


        
        