from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        my_count ,left = 0 ,0
        for right in range(len(s)):
            while s[right] in seen :
                seen.remove(s[left])
                left +=1

            seen.add(s[right])
            my_count = max(my_count,right-left+1)


        return my_count
    
class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_l = 0 
        q = deque()

        for c in s:
            if c in q :
                while q.popleft() != c:
                    pass

            q.append(c)
            max_l = max(max_l,len(q))

        return max_l
