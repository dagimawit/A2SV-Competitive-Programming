class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        indices = {}
        for i in range(len(list1)):
            indices[list1[i]] = i

        min_sum = float('inf')
        result = []

        for j in range(len(list2)):
            if list2[j] in indices:
                current_sum = j + indices[list2[j]]
                if current_sum < min_sum:
                    min_sum = current_sum
                    result = [list2[j]]
                elif current_sum == min_sum:
                    result.append(list2[j])

        return result