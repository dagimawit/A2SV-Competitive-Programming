class Solution(object):
    def largestOddNumber(self, num):
        largest_odd = ""
        n = len(num)

        for i in range(n - 1, -1, -1):
            if int(num[i]) % 2 != 0:
                largest_odd = num[:i+1]
                break

        return largest_odd