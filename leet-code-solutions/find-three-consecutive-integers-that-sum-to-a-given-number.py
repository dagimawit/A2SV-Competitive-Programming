class Solution(object):
    def sumOfThree(self, num):
        start = (num - 1) // 3
        if start + start + 1 + start + 2 == num:
            return [start, start + 1, start + 2]
        return []