from typing import List


# This solution take t.c. O(n) and s.c. O(1) , because we are using a dictionary to store the frequency of the fruits and we are using two pointers to find the maximum window size which is less than or equal to 2. So we are doing just one pass through the
class bestSolution:
    def totalFruit(self, fruits: List[int]) -> int:
        if len(fruits) <= 2:
            return len(fruits)
        
        freq = {}
        left , maxi = 0, 0
        for right in range(0,len(fruits)):
            freq[fruits[right]] = freq.get(fruits[right],0) +1

            if len(freq) > 2 :
                freq[fruits[left]] -= 1

                if freq[fruits[left]] == 0 :
                    del freq[fruits[left]]

                left +=1

            if len(freq) <= 2 :
                maxi = max(maxi,right-left+1) 

        return maxi
    
# here the key thing is , we are not chaining the window size , we are just checking it that why we put the condition of freq is <= 2 

# take O(2n) 
class better:
    def totalFruit(self, fruits: List[int]) -> int:
        if len(fruits) <= 2:
            return len(fruits)
        
        freq = {}
        left , maxi = 0, 0
        for right in range(0,len(fruits)):
            freq[fruits[right]] = freq.get(fruits[right],0) +1

            while len(freq) > 2 :
                freq[fruits[left]] -= 1

                if freq[fruits[left]] == 0 :
                    del freq[fruits[left]]

                left +=1

            
            maxi = max(maxi,right-left+1) 

        return maxi