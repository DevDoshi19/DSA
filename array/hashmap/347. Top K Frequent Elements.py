from collections import Counter
import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        freq = Counter(nums)

        for key,value in freq.items():
            heapq.heappush(heap,[value,key])

            if len(heap) > k :
                heapq.heappop(heap)

        return [key for _,key in heap]
