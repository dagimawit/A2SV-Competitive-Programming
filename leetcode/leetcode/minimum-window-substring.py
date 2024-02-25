class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == t:
            return s
        ans = ""
        mapT = {}  # frequency of t
        for ch in t:
            mapT[ch] = mapT.get(ch, 0) + 1

        mct = 0  # match count
        dmct = len(t)  # desired match count
        mapS = {}
        i = -1
        j = -1

        while True:
            f1 = False
            f2 = False

            # Acquire the character
            while i < len(s) - 1 and mct < dmct:
                i += 1
                ch = s[i]
                mapS[ch] = mapS.get(ch, 0) + 1

                if mapS.get(ch, 0) <= mapT.get(ch, 0):
                    mct += 1
                f1 = True

            # Collect answers and release
            while j < i and mct == dmct:
                j += 1
                pans = s[j:i + 1]  # pans = potential answer
                if not ans or len(pans) < len(ans):
                    ans = pans

                ch = s[j]
                if mapS[ch] == 1:
                    del mapS[ch]
                else:
                    mapS[ch] -= 1

                if mapS.get(ch, 0) < mapT.get(ch, 0):
                    mct -= 1
                f2 = True

            if not f1 and not f2:
                break
        return ans