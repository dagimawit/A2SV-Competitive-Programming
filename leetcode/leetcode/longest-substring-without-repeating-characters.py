class Solution:
    def lengthOfLongestSubstring(self, S: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(S)):
            while S[r] in charSet:
                charSet.remove(S[l])
                l += 1
            charSet.add(S[r])
            res= max(res, r - l + 1)
        return res

