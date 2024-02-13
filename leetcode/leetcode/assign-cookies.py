class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i=0
        j=0
        content_children=0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                content_children+=1
                i+=1
            j+=1
        return content_children
        # # g.sort()
        # # s.sort()
        # count = 0
        # j = 0
        # for i in  range(len(g)):
        #     while j < len(s) and s[j] < s[i]:
        #         j +=1
        #     if j < len(s):
        #         count +=1
        #         j+=1
        #     else:
        #         break
        # return count