class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        max_candies = max(candies)  # Find the maximum number of candies
        output = []
        
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max_candies:
                output.append(True)
            else:
                output.append(False)
        
        return output