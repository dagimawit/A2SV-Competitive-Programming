from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        stack = []
        for bill in bills:
            if bill == 5:
                stack.append(bill)
            elif bill == 10:
                if 5 in stack:
                    stack.remove(5)
                    stack.append(10)
                else:
                    return False
            else:  # bill == 20
                if 10 in stack and 5 in stack:
                    stack.remove(10)
                    stack.remove(5)
                elif stack.count(5) >= 3:
                    stack.remove(5)
                    stack.remove(5)
                    stack.remove(5)
                else:
                    return False
        
        return True