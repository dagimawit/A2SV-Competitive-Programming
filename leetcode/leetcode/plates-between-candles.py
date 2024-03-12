class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n,m=len(s),len(queries)
        total_plates=[0]*n
        left,right=[-1]*n,[-1]*n
        for i,c in enumerate(s):
            if i==0: continue
            if c=='*': total_plates[i]=total_plates[i-1]+1
            else: total_plates[i]=total_plates[i-1]
        right_latest,left_latest=-1,-1
        for i,c in enumerate(s):
            if c=='|': right_latest=i
            right[i]=right_latest
        for i in range(n-1,-1,-1):
            c=s[i]
            if c=='|': left_latest=i
            left[i]=left_latest
        ans=[0]*m
        for i,(l,r) in enumerate(queries):
            left_plate,right_plate=left[l],right[r]
            if left_plate==-1 or right_plate==-1 or (left_plate>=right_plate):
                continue
            val=total_plates[right_plate]-total_plates[left_plate]
            ans[i]=val
        return ans