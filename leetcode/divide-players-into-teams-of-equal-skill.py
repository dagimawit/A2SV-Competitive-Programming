class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        l = 0
        r = len(skill) - 1
        skill.sort()
        result = []
        theSum = []
        total = []
        while(l < r):
            temTuple = (skill[l], skill[r])
            result.append(temTuple)
            l +=1
            r -=1
        for temTuple in result:
            theSum.append(temTuple[0] + temTuple[1])
        if len(set(theSum)) == 1:
            total = sum(x * y for x, y in result)
            return total
        else:
            return -1


        