class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        answer = []
        for i in range(len(image)):
            answer.append(map(lambda x:1 if x ==0 else 0,list(reversed(image[i]))))

        return answer
        