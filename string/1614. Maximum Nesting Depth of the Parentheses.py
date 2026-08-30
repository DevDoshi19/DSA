class Solution:
    def maxDepth(self, s: str) -> int:
    
        count = 0
        max_count = 0 
        for i in range(len(s)):
            if s[i] == "(" :
                count += 1 
            if s[i] ==")":
                count -= 1 

            max_count = max(max_count,count)

        return max_count 