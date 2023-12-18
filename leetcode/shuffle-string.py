class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        dictionary = {index: value for index, value in zip(indices, s)}
        sorted_list = [dictionary[key] for key in sorted(dictionary.keys())]
        return "".join(sorted_list)
