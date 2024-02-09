class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        left = 0
        right = n-k
        max_score = sum(cardPoints[right:])
        
        currscore = max_score
        for i in range(k):
            currscore += cardPoints[left + i] - cardPoints[right + i]
            max_score = max(max_score, currscore)

        return max_score
    
#     1 2 3 4 5 6 1
# curScore +1  - 5 = 8
#  12 +2 - 6= 8
#  12 +3 - 1 = 14