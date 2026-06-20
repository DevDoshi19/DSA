# this question want to tell that : 
"""
picking up the k card whether form the start of the array or the end of the array  in a way that they should able to give us the
maximum number of points , so we are first go from 0 index to k , for 1st element , then we do same for the right side of the array.    

"""
from typing import List

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        if n == k :
            return sum(cardPoints)

        maxi =0 
        total =0
        i = 0
        j = n-1
        while i < k :
            total += cardPoints[i]
            i+=1

        i-=1
        maxi = total
        while i >= 0 :
            total += cardPoints[j] - cardPoints[i]
            maxi = max(maxi,total)
            i -= 1
            j -= 1

        return maxi
            
# same as O(2n) , Because example the array len is 7 and k = 6 , so 1st loop itreate over 6 and then 2 loop itrate over another 6 [delete form the left side and add from  the right side ]

# solution 2
class betterSolution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        if n == k :
            return sum(cardPoints)

        left_sum , right_sum = 0,0
        for i in range(0,k) :
            left_sum += cardPoints[i]

        
        maxi = left_sum
        right_ind = n-1
        i = k -1
        while i >= 0 :

            left_sum = left_sum - cardPoints[i]
            right_sum = right_sum + cardPoints[right_ind]
            maxi = max(maxi,right_sum+left_sum)
            i-=1
            right_ind -=1

        return maxi 
    
# t.c. O(2k) and s.c. O(1) because we are using just two variable to store the sum of left and right side and we are using two pointers to find the maximum score. So we are doing just one pass through the array.