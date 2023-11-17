class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = 0
        prefix_sums = collections.defaultdict(int)
        prefix_sums[0] = 1
        window_sum = 0

        for num in nums:
            window_sum += num
            count += prefix_sums[window_sum - goal]
            prefix_sums[window_sum] += 1

        return count