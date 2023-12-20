class Solution:
    def __init__(self):
        self.oneChance = True
    
    def checkPowersOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        if not n % 3:
            return self.checkPowersOfThree(n // 3)
        elif n % 3 == 1:
            self.oneChance = False
            return self.checkPowersOfThree((n - 1) // 3)
        return False
        