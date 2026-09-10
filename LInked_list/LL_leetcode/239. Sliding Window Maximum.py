from collections import deque
from typing import List

# brute force approach o(n*k) time complexity and o(k) space complexity
class Solution1:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums :
            return []
        if k > len(nums):
            return []

        n = len(nums)
        queue = deque()
        ans = []
        
        for i in range(k):
            queue.append(nums[i])
        
        maxi = max(queue)
        ans.append(maxi)

        for i in range(k,n):
            queue.popleft()
            queue.append(nums[i])
            maxi = max(queue)
            ans.append(maxi)

        return ans            

class Solution2:
    # more optimized approach using deque to store indices of elements in the current window
    # time complexity is O(n) and space complexity is O(k)
    # pattren : monotonic queue -> use to store indices of elements in the current window and maintain the order of elements in decreasing order
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums :
            return []
        if k > len(nums):
            return []

        q = deque()   # stores indices; values are kept in decreasing order
        ans = []

        for i in range(len(nums)):

            # Remove indices that are outside the current window.
            if q and q[0] <= i - k:
                q.popleft()

            # Any smaller value behind nums[i] can never become maximum
            # while nums[i] is still in the window.
            while q and nums[q[-1]] <= nums[i]:
                q.pop()

            q.append(i)

            # A full window is formed starting from i = k - 1.
            if i >= k - 1:
                ans.append(nums[q[0]])

        return ans