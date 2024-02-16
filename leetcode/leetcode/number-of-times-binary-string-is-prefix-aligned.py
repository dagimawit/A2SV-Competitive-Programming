class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        count = 0
        max_sum = 0
        total_sum = 0
        for i in range(len(flips)):
            total_sum += flips[i]
            if total_sum == (i + 1) * (i + 2) / 2:
                count += 1
        return count
