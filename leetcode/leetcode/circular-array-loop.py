class Solution:
    def next(self, nums, current):
        return (nums[current] + current + len(nums)) % len(nums)


    def circularArrayLoop(self, nums: List[int]) -> bool:
        for i, val in enumerate(nums):
            count = 0
            pointer = i
            while not ((nums[pointer] > 0) ^ (val > 0)) and count <= len(nums):
                if pointer == self.next(nums, pointer):
                    break
                pointer = self.next(nums, pointer)
                count += 1
            if count >= len(nums):
                return True

        return False