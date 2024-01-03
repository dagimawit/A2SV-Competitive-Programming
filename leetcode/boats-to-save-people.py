class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        l = 0
        n = len(people)
        r = len(people) - 1
        people.sort(reverse=True)
        limit;
        result = []
        while(l<r):
            if people[l] == limit:
                tempTuple = (people[l])
                result.append(tempTuple)
                l +=1
            elif people[l] + people[r] <= limit:
                tempTuple = (people[l],people[r])
                result.append(tempTuple)
                l +=1
                r -=1
            elif people[l] + people[r]> limit:
                tempTuple = (people[l])
                result.append(tempTuple)
                l +=1
        if l ==r:
            tempTuple = (people[l])
            result.append(tempTuple)
        count = 0
        for i in result:
            count +=1
        return count
