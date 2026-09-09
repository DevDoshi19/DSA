from typing import List

class Solution:

    """
    - Binary Search on Answer:
    1. k can range from 1 to max(piles). For each k, calculate total hours needed.
    2. If hours <= h, k works -> try smaller k: high = k.
    3. If hours > h, k is too slow -> try bigger k: low = k + 1.
    4. Finally, low is the minimum eating speed that works.
    """
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_k,max_k = 1,max(piles)
        while min_k < max_k :
            k = (min_k+max_k) // 2 
            hours = 0
            for i in piles :
                hours += (i + k -1 ) // k
            if hours <= h :
                max_k = k 
            elif hours > h :
                min_k = k + 1  

        return min_k