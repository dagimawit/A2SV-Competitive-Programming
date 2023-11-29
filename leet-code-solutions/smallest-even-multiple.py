class Solution(object):
    def smallestEvenMultiple(self, n):
        minm = n
        small = 2 * n
        
        if n % 2 == 0:
            return n
        return small
        
        