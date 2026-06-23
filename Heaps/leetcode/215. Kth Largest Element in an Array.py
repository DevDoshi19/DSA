import heapq
import random
from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        def heapify(nums, n, i):
            largest_index = i
            left_index = 2 * i + 1
            right_index = 2 * i + 2

            if left_index < n and nums[left_index] > nums[largest_index]:  
                largest_index = left_index

            if right_index < n and nums[right_index] > nums[largest_index]:  
                largest_index = right_index

            if largest_index != i:
                nums[i], nums[largest_index] = nums[largest_index], nums[i]
                heapify(nums, n, largest_index)

        def heapsort(nums, k):
            n = len(nums)

            # Build max heap
            for i in range(n // 2 - 1, -1, -1):
                heapify(nums, n, i)

            # Pop k times
            for last_index in range(k):
                nums[0], nums[n - last_index - 1] = nums[n - last_index - 1], nums[0]
                heapify(nums, n - last_index - 1, 0)

        heapsort(nums, k)
        return nums[len(nums) - k] 
    
    """
    Complexity
    Time  O(n log n) 
    Space O(1)  - in place 
    """
    
class Solution2:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)

        return nums[k-1]
    
class Solution3:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []

        for num in nums:
            heapq.heappush(min_heap, num)      # push element
            if len(min_heap) > k:
                heapq.heappop(min_heap)         # remove smallest

        return min_heap[0]
    
    """
    Complexity
    Time  O(n log k) — better than O(n log n)!
    Space O(k)
    """

# You can actually solve this in O(n) average using QuickSelect algorithm — same idea as quicksort's partition. Worth knowing!

class Solution4:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums: 
            return
        pivot = random.choice(nums)
        left =  [x for x in nums if x > pivot]
        mid  =  [x for x in nums if x == pivot]
        right = [x for x in nums if x < pivot]
        
        L, M = len(left), len(mid)
        
        if k <= L:
            return self.findKthLargest(left, k)
        elif k > L + M:
            return self.findKthLargest(right, k - L - M)
        else:
            return mid[0]

# solution 5 using quick select algorithm
class Solution5:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        left ,right = 0 ,len(nums)-1
        while True:
            pivot_index = random.randint(left,right)
            pivot_index = self.partition(nums,left,right,pivot_index)
            if pivot_index == k-1:
                return nums[pivot_index]
            elif pivot_index < k-1:
                left = pivot_index + 1
            else:
                right = pivot_index - 1
        
    def partition(self,nums,left,right,pivot_index):
        pivot_value = nums[pivot_index]
        # move pivot to end
        nums[pivot_index],nums[right] = nums[right],nums[pivot_index]
        store_index = left
        for i in range(left,right):
            if nums[i] > pivot_value:
                nums[store_index],nums[i] = nums[i],nums[store_index]
                store_index += 1
        # move pivot to its final place
        nums[right],nums[store_index] = nums[store_index],nums[right]
        return store_index
    
# But there is an edge case where the pivot is always the smallest or largest element, which will lead to O(n^2) time complexity. To avoid this, we can use the median of medians algorithm to select a good pivot in O(n) time.
