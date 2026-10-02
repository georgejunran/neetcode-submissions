class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        array_sum = {}

#possible to use the enumerate function which iterates the array
        for i, n in enumerate(nums):
            diff = target - n
            if diff in array_sum:
                return [array_sum[diff], i] 
            array_sum[n] = i 