# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 0
        right = n-1
        while left <= right:
            mid =  (left + right)//2
            if isBadVersion(mid) == False:
                left = mid +1
            elif isBadVersion(mid) == True:
                right = mid -1
            elif left == right and isBadVersion(left) == True:
                return left
        return left
