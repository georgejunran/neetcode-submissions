#Bucketsort solution 
#Time complexity O(n)
#Memory complexity O(n)
# class Solution:
#     def topKFrequent(self, nums: list[int], k: int) -> list[int]:
#         amount = {}
#         times = [[] for i in range(len(nums) + 1)]
#         result = []

        #count the amount of times each value occurs
        # for n in nums:
        #     amount[n] = 1 + amount.get(n, 0)
        # for n, c in amount.items():
        #     times[c].append(n)

        #sort the numbers that occur frequently into results
        # for i in range(len(times) - 1, 0, -1):
        #     for n in times[i]:
        #         result.append(n)
        #         if len(result) == k:
        #            return result

#heaps solution minheap
#Time complexity O(nlogk)
#Memory complexity O(n)
import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        heap = []
        counter = Counter(nums)

        for key, value in counter.items():
            if len(heap) < k:
                heapq.heappush(heap, (value, key))
            else: 
                heapq.heappushpop(heap, (value, key))   

        return [h[1] for h in heap]  