class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        differnce = []
        for cav, cbv in costs:
            differnce.append([cbv-cav, cav,cbv])
        differnce.sort()
        result = 0
        for i in range(len(differnce)):
            if i < len(differnce)//2:
                result += differnce[i][2]
            else:
                result += differnce[i][1]
        return result


        