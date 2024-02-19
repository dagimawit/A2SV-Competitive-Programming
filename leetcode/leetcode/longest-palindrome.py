class Solution:
    def longestPalindrome(self, s: str) -> int:
        maximum_length = 0
        seen = set()
        
        for char in s:
            if char in  seen:
                maximum_length +=2
                seen.remove(char)
            else:
                seen.add(char)
        return maximum_length + bool(seen)