class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
#possible to just sort both lists and compare
        # return sorted(s) == sorted(t)

#if not sorted
        sarray, tarray = {}, {}
        
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            sarray[s[i]] = 1 + sarray.get(s[i], 0)
            tarray[t[i]] = 1 + tarray.get(t[i], 0)
        return Counter(s) == Counter(t)
#if not using the Counter function in Python
        # for l in sarray:
        #     if sarray[l] != tarray.get(l, 0):
        #         return False

        return True