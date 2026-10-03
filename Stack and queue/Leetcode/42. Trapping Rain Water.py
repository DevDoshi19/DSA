"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
"""

class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        maxleft = [0]*n
        maxright = [0]*n 
        maxi = float("-inf")

        for i in range(n):
            maxi = max(maxi,height[i])
            maxleft[i] = maxi
        
        maxi = float("-inf")
        for i in range(n-1,-1,-1):
            maxi = max(maxi,height[i])
            maxright[i] = maxi
            
        result = 0
        for i in range(n):
            mini = min(maxleft[i],maxright[i])
            result += abs(height[i] - mini)

        return result

class Solution2:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        start = 0 
        end = n-1 

        leftmax = 0 
        rightmax = 0
        totalmax = 0

        while start<end:
            leftmax = max(leftmax,height[start])
            rightmax = max(rightmax,height[end])

            if leftmax < rightmax:
                totalmax += leftmax-height[start]
                start += 1
            else :
                totalmax += rightmax-height[end]
                end -=1

        return totalmax
    
class Solution3:
    def trap(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1

        left_max = 0
        right_max = 0
        water = 0

        while left <= right:

            if height[left] <= height[right]:

                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water += left_max - height[left]

                left += 1

            else:

                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]

                right -= 1

        return water
