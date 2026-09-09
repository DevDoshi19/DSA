from typing import List

"""
Normal BS       → compare target
Lower bound     → find boundary
Rotated array   → identify sorted half
Single element  → identify index/pairing property

Before single:
[even, odd] [even, odd] [even, odd]

After single:
[odd, even] [odd, even] [odd, even]
"""

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0] 
        
        low,high = 0,n-1
        while low < high :
            cal = ((low+high)//2)
            mid = cal if cal%2 == 0 else cal-1
            if nums[mid] == nums[mid+1] :
                low = mid + 2
            else :
                high = mid  
            
        return nums[low]
    
s = Solution()
# s.singleNonDuplicate([1,1,2,3,3,4,4,8,8])
print(s.singleNonDuplicate([3,3,7,7,10,11,11]))


"""
[mid, mid+1] = valid pair

Look at the array before the single element
index:  0  1  2  3  4  5  6  7
value:  1  1  2  2  3  4  4  5
                       ↑
                    single

Before the single element, pairs start at:

0, 2, 4, ...

So they look like:

[0,1] [2,3] [4,5] [6,7]

But after the single element, everything shifts by one:

[0,1] [2,3] [4] [5,6] [7,8]
                 ↑
              shifted

That's the property you want to exploit.
"""