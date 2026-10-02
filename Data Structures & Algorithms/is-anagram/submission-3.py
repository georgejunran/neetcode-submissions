class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
#possible to just sort both lists and compare
        return sorted(s) == sorted(t)