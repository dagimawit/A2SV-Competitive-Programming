import numpy as np
class Solution:
    def maxSum(self, grid) -> int:
        l, r, m, n = 0, 0, len(grid), len(grid[0])
        arr = np.array(grid)
        max_sum = 0
        while l < m - 2:
            while r < n - 2:
                current_sum = np.sum(arr[l:l + 3, r:r + 3]) - (arr[l + 1, r] + arr[l + 1, r + 2])  # summing 3x3 matrix and subtracting 2 values
                max_sum = max(max_sum, current_sum)
                r += 1
            l += 1
            r = 0
        return max_sum