"""
Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.
In one move, you can increment n - 1 elements of the array by 1.

Example 1:

Input: nums = [1,2,3]
Output: 3
Explanation: Only three moves are needed (remember each move increments two elements):
[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
Example 2:

Input: nums = [1,1,1]
Output: 0
"""

class Solution:
    def minMoves(self, nums: list[int]) -> int:
        total = 0 
        mini = min(nums)
        for num in nums :
            total += num - mini

        return total 
class Solution2:
    def minMoves(self, nums: list[int]) -> int:
        total = sum(nums) 
        mini = min(nums)
        
        return total - len(nums) * mini 
    
# T.c. = O(n)
# S.c. = O(1)

# the main idea is to find the minimum number in the array and then calculate the total number of moves required to make all elements equal to that minimum value. Each move consists of incrementing n - 1 elements, which effectively means we are reducing the difference between the maximum and minimum values in the array.

"""
When an operation affects n-1 elements, try thinking about the one element that is NOT affected.

We are NOT actually decrementing all n-1 elements in the original operation.

Let's go slowly.
1. Original operation
Array:
nums = [5, 5, 5, 10]

Rule: In one move, increment exactly n-1 elements by 1.

Since n = 4, we increment 3 elements every time.

For example:
Initial: [5, 5, 5, 10]

Move 1:  [6, 6, 6, 10]
Move 2:  [7, 7, 7, 10]
Move 3:  [8, 8, 8, 10]
Move 4:  [9, 9, 9, 10]
Move 5:  [10, 10, 10, 10]

Answer = 5 moves.

Notice that we never incremented the last element. We incremented the other three.

Instead of incrementing 3 elements, imagine decrementing the remaining 1 element.

Why does this work?

Compare the two operations:
Original operation	Equivalent operation
[5,5,5,10]	[5,5,5,10]
[6,6,6,10]	[5,5,5,9]
[7,7,7,10]	[5,5,5,8]
[8,8,8,10]	[5,5,5,7]
[9,9,9,10]	[5,5,5,6]
[10,10,10,10]	[5,5,5,5]

Both represent the same relative differences between elements.

This is the important part:

We can choose ANY ONE element to decrement in the transformed version.

We don't need to decrement n-1 elements.
"""