class Solution(object):
    def isPalindrome(self, x):
        num_str = str(x)

        return num_str == num_str[::-1]
        