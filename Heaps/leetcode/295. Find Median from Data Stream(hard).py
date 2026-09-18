import heapq

# Use two heaps to split numbers into a smaller half and a larger half.
# smallValues is a max-heap (using negative values) → gives largest of smaller half.
# largeValues is a min-heap → gives smallest of larger half.
# Maintain: max(small) <= min(large), so the median is at the boundary.
# Keep heap sizes balanced: their sizes can differ by at most 1.
# If ordering breaks, move the top element from small to large.
# If one heap becomes too large, move its top element to the other heap.
# Odd count → median is top of the larger heap; even → average of both tops.
# addNum() = O(log n), findMedian() = O(1), space = O(n).

class MedianFinder:

    def __init__(self):
        self.smallValues = []
        self.largeValues = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.smallValues,-num)
        if self.smallValues and self.largeValues and (-self.smallValues[0] > self.largeValues[0] ):
            e = -heapq.heappop(self.smallValues)
            heapq.heappush(self.largeValues,e)

        if len(self.smallValues) > len(self.largeValues)+1:
            val = -heapq.heappop(self.smallValues)
            heapq.heappush(self.largeValues,val)
        if len(self.smallValues)+1 < len(self.largeValues):
            val = heapq.heappop(self.largeValues)
            heapq.heappush(self.smallValues,-val)

    def findMedian(self) -> float:
        if len(self.smallValues) > len(self.largeValues):
            return float(-self.smallValues[0])
        elif len(self.smallValues) < len(self.largeValues):
            return float(self.largeValues[0])

        return (-self.smallValues[0] + self.largeValues[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()