import heapq
from typing import List
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if not points:
            return []

        heap = []
        for x1,y1 in points:
            distance = ((x1)**2 + (y1)**2) 
            heapq.heappush(heap,[distance,[x1,y1]])

        ans = []
        for i in range(k):
            dis,point = heapq.heappop(heap)
            ans.append(point)

        return ans