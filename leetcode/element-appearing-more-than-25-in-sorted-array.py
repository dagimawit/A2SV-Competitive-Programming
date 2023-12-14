class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        freq = len(arr) // 4 + 1
        result = {}

        for i in range(len(arr)):
            result[arr[i]] = result.get(arr[i], 0) + 1

            if result[arr[i]] >= freq:
                return arr[i]

        return -1 
        