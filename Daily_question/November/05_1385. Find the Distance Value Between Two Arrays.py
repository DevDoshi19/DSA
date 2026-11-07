from bisect import bisect


class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        ans = 0
        for num1 in arr1:
            isTrue = True
            for num2 in arr2:
                if abs(num1 - num2) <= d :
                    isTrue = False
                    break

            if isTrue :
                ans += 1

        return ans
    

# optimal using binary search
class Solution2:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr2.sort()
        ans = 0
        for num in arr1 :

            index = bisect.bisect_left(arr2,num-d)
            if index < len(arr2) and arr2[index] <= num+d :
                continue
                
            ans+=1

        return ans