from typing import List

class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        prefix = 0
        seen_at = {}
        max_len = 0

        for i, hour in enumerate(hours):
            if hour > 8:
                prefix += 1
            else:
                prefix -= 1

            if prefix > 0:
                max_len = i + 1

            if prefix - 1 in seen_at :
                max_len = max(max_len, i - seen_at [prefix - 1])

            if prefix not in seen_at :
                seen_at [prefix] = i

        return max_len