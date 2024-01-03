class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        column = len(strs[0])
        for c in range(column):
            for i in range(len(strs)-1):
                if strs[i][c] > strs[i+1][c]:
                    count+=1
                    break
        return count