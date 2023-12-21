class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        value = list(zip(*matrix))
        for i in range(len(value)):
            matrix[i] = reversed(value[i])
        