class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        covered = [False] * 51  # Initialize a boolean array to mark coverage

        for start, end in ranges:
            for i in range(start, end + 1):
                covered[i] = True  # Mark each integer within the range as covered

        for i in range(left, right + 1):
            if not covered[i]:
                return False
        return True