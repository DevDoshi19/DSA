class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        # odd = sum(p & 1 for p in accumulate(arr))  
        # return odd * (len(arr) + 1 - odd) % (10**9 + 7) 
        n = len(arr)
        prefix = 0
        even_sum = 1 # taking 0 as start for the even number cause we want to calculate the single odd number  
        odd_sum = 0
        count = 0
        MODULO = 10**9 + 7 
        for i in range(n):
            prefix += arr[i]

            if prefix % 2 == 0 :
                # count the odd number till now , cause odd + even = odd
                count = (count + odd_sum) % MODULO
                even_sum += 1
            else:
                # even + odd = odd , so we are adding even till now we have seen.  
                count = (count + even_sum) % MODULO
                odd_sum += 1

        return count