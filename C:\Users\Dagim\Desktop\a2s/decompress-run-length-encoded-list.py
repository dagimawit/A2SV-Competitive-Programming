class Solution(object):
    def decompressRLElist(self, nums):
        decompressed = []
        n = len(nums)

        for i in range(0, n, 2):
            freq = nums[i]
            val = nums[i+1]
            sublist = [val] * freq
            decompressed.extend(sublist)

        return decompressed