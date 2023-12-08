class Solution(object):
    def printVertically(self, s):
        words = s.split()
        max_len = max(len(word) for word in words)
        result = []
        for i in range(max_len):
            word = ""
            for j in range(len(words)):
                if i < len(words[j]):
                    word += words[j][i]
                else:
                    word += " "
            result.append(word.rstrip())
        return [word.rstrip() for word in result if word.strip()]  