class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_length = 0
        longest_sequence = []

        for num in nums:
            if num - 1 not in num_set:
                current_length = 1
                current_sequence = [num]
                while num + 1 in num_set:
                    num += 1
                    current_length += 1
                    current_sequence.append(num)

                if current_length > max_length:
                    max_length = current_length
                    longest_sequence = current_sequence

        return len(longest_sequence)
        