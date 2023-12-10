class Solution(object):
    def largestGoodInteger(self, num):
        max_good_integer = ""

        for i in range(len(num) - 2):
            substring = num[i:i+3]
            if len(set(substring)) == 1:
                max_good_integer = max(max_good_integer, substring)

        if max_good_integer == "":
            return ""

        return max_good_integer
