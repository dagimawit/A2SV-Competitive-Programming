class Solution:
    def sortSentence(self, s: str) -> str:
        
        array = s.split(" ")
        sorted_arr = sorted(array, key=lambda x: int(x[-1]))
        answer = " ".join([string[:-1] for string in sorted_arr])
        return answer
        # return "".join(answer)
  
