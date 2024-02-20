class Solution(object):
    def countGoodNumbers(self, n):
        m = 10**9 + 7
        if n ==1:
            return 5
        elif n% 2 ==0:
            return (pow(5,n//2,m) * pow(4,n//2,m)) %m
        elif n %2 !=0:
            return (pow(5,((n +1) //2),m) * pow(4,((n//2)),m)) % m
            