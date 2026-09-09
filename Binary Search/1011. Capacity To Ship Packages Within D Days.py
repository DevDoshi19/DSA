from typing import List

class Solution:

    """
    Given an array weights and an integer days, we need to ship all the packages within days. We can ship packages in order and we can only ship packages with a total weight less than or equal to capacity. We need to find the minimum capacity of the ship that will allow us to ship all packages within days.

    # Binary Search on Answer:
    # Capacity ranges from max(weights) to sum(weights).
    # For each capacity, count how many days are needed to ship all packages in order.
    # If days_needed <= days, capacity works -> try a smaller capacity: high = capacity.
    # If days_needed > days, capacity is too small -> increase it: low = capacity + 1.
    # Finally, low is the minimum capacity that can ship all packages within the given days.
    """
    def countDays(self,capacity:int,weights:List[int])->int:
        days,current_weight = 1,0
        for weight in weights :
            if current_weight + weight > capacity:
                days+= 1
                current_weight = weight
            else :
                current_weight += weight
                
        return days 

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)

        while low < high :
            capacity = (low+high) // 2
            d = self.countDays(capacity,weights)
            if d <= days:
                high = capacity
            else :
                low = capacity + 1 
        
        return low 
    
"""
Koko:

speed too slow → go right
speed works → go left

Shipping:

capacity too small → go right
capacity works → go left

The story changes, but the binary-search pattern is identical.
"""