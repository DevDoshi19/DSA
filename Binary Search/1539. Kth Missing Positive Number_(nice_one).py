from typing import List
class Solution:
    # t.c. = O(n), s.c. = O(1)
    def findKthPositive(self, arr: List[int], k: int) -> int:
    # We treat k as the current candidate value for the k-th missing positive number.
    # If arr contains a number <= k, that number is NOT missing, so our answer must move forward.
    # Therefore, whenever num <= k, we increase k by 1.
    # We use <= because even if num == k, k itself exists and cannot be the missing answer.
    # Since arr is sorted, once num > k, all following numbers are also > k, so we can stop.
    # Example: arr=[2,3,4,7,11], k=5 -> k becomes 6 -> 7 -> 8 -> 9, so answer = 9.
    # This is basically brute-force counting compressed into a simple adjustment of k.
        for num in arr:
            if num <= k:
                k += 1
            else:
                break
        return k

# solution 2 : Binary Search => t.c. = (logn), s.c. = O(1)
class Solution2:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            # The number of missing positive integers before arr[mid] is arr[mid] - (mid + 1)
            missing = arr[mid] - (mid + 1) 
            if missing < k:
                left = mid + 1
            else:
                right = mid - 1
        return left + k