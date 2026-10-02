class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        array_sum = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in array_sum:
                return [array_sum[diff], i] 
            array_sum[n] = i 