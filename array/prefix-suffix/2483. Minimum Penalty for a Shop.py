class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        n = len(customers)
        prefix_n = [0] * (n + 1)
        suffix_y = [0] * (n + 1)

        for i in range(n):
            prefix_n[i + 1] = prefix_n[i] + (customers[i] == "N")

        for i in range(n - 1, -1, -1):
            suffix_y[i] = suffix_y[i + 1] + (customers[i] == "Y")

        mini_pentaly = float("inf") 
        index = -1
        for j in range(0,n+1):
            pentaly = prefix_n[j] + suffix_y[j]
                    
            if mini_pentaly > pentaly :
                index = j 
                mini_pentaly = pentaly 

        return index

"""
Complexity
- Time: O(n)
- Auxiliary space: O(n) for the two arrays.
"""

# approch 2: Using only one pass and constant space
class Solution2:
    def bestClosingTime(self, customers: str) -> int:
        max_score = 0
        current_score = 0
        best_hour = 0
        
        for i, ch in enumerate(customers):
            if ch == 'Y':
                current_score += 1
            else:
                current_score -= 1
                
            if current_score > max_score:
                max_score = current_score
                best_hour = i + 1
                
        return best_hour

"""
Complexity
- Time: O(n)
- Auxiliary space: O(1)
"""

# Apporach 3: Using only one pass and constant space
class Solution3:
    def bestClosingTime(self, customers: str) -> int:
        # Start by assuming we close at hour 0.
        # The initial penalty is the total number of 'Y's in the string.
        current_penalty = customers.count('Y')
        min_penalty = current_penalty
        best_hour = 0
        
        # Iterate through each possible closing hour from 1 to n
        for i, status in enumerate(customers):
            if status == 'Y':
                current_penalty -= 1  # We closed, so we missed this customer (penalty decreases)
            else:
                current_penalty += 1  # We stayed open, but no customer came (penalty increases)
            
            # Check if this closing hour gives a strictly smaller penalty
            if current_penalty < min_penalty:
                min_penalty = current_penalty
                best_hour = i + 1
                
        return best_hour
