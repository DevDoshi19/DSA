from typing import List

"""
Time Complexity: O(1) — because there are at most (3^4 = 81) candidate partitions, and the input length is bounded by 12.
Auxiliary Space Complexity: O(1) — recursion depth and current partition are limited to 4 segments.

Output Space: O(1) under the same input constraint, since the number and size of valid IP addresses are bounded.
"""

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) < 4 or len(s) > 12:
            return []
        
        result = []

        def solve(index, lst):
            if len(lst) == 4:
                if index == len(s):
                    result.append(".".join(lst))
                return

            for i in range(index, len(s)):
                ip = s[index:i+1]

                if len(ip) > 3:
                    break

                if len(ip) > 1 and ip[0] == "0":
                    continue

                if int(ip) <= 255:
                    lst.append(ip)
                    solve(i+1, lst)
                    lst.pop()

        solve(0, [])
        return result