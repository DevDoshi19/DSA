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