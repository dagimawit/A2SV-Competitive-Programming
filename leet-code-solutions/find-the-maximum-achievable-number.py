class Solution(object):
    def theMaximumAchievableX(self, num, t):
        result = num + 2*t
        return max(result,num)
        
        