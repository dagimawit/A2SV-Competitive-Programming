class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        best =10 **20
        current = 0
        n = len(blocks)
        for i in range(n):
            if blocks[i] =='W':
                current +=1
            if i-k >=0 and blocks[i-k] == 'W':
                current -=1
            if i -k +1 >=0:
                best = min(best,current)
        return best