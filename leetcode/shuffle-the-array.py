class Solution(object):
     def shuffle(self, nums, n):
        new = []
        for i in range(n):
            new.append(nums[i])
            new.append(nums[n])
            n+=1
        return new
        