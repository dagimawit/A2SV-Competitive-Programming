class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = 0
        can = capacity
        for i in range(len(plants)):    
            if can < plants[i]:
                steps = steps + 2 * i + 1
                can = capacity
                can -= plants[i]
            else: 
                steps = steps + 1
                can -= plants[i]
        return steps
        