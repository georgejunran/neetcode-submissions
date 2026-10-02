class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        If_Dupe = set()
        
        for i in nums:
            if i in If_Dupe:
                return True
            If_Dupe.add(i)
        return False