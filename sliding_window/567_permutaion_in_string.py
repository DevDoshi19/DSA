from typing import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        left = 0
        s1_count = Counter(s1)
        window = Counter(s2[0:len(s1)])

        for i in range(len(s1), len(s2)):
            if window == s1_count:
                return True
            else:
                window = Counter(s2[left+1:i+1])  # ✅ fixed slice
                left += 1

        return window == s1_count  # ✅ check last window