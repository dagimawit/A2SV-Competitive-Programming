class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        l = 0
        r = len(piles) - 1
        piles.sort(reverse =True)
        result = []
        total= 0
        while(l<r):
            small_Tuples = (piles[l],piles[l+1],piles[r])
            result.append(small_Tuples)
            l +=2
            r -=1
        for small_Tuples in result:
            total += small_Tuples[1]
        return total
        