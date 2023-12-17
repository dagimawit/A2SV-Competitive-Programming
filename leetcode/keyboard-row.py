class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        s1 = "qwertyuiop"
        s2 = "asdfghjkl"
        s3 = "zxcvbnm"
        answer = []
        for word in words:
            row = None
            for char in word:
                if char.lower() in s1:
                    if row is None:
                        row = 1
                    elif row != 1:
                        row = -1
                        break
                elif char.lower() in s2:
                    if row is None:
                        row = 2
                    elif row != 2:
                        row = -1
                        break
                elif char.lower() in s3:
                    if row is None:
                        row = 3
                    elif row != 3:
                        row = -1
                        break
            if row != -1:
                answer.append(word)
        return answer