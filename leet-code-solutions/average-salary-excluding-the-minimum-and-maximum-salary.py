from decimal import Decimal
class Solution(object):
    def average(self, salary):
        salary.sort()
        theirsum = Decimal(0)
        newsalary = salary[1:-1]
        for i in range(len(newsalary)):
            theirsum += Decimal(newsalary[i])
        avg = theirsum / Decimal(len(newsalary))
        avg = round(avg, 5)  # Round the average to 5 decimal places
        return avg
            
        