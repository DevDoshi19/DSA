from collections import defaultdict


class Solution:
    def groupThePeople(self, groupSizes: list[int]) -> list[list[int]]:

        mp = defaultdict(list)
        ans = []
        for index,group in enumerate(groupSizes):
            mp[group].append(index)

            if len(mp[group]) == group :
                ans.append(mp[group])
                mp[group] = []

        return ans 
    
"""
Time complexity: O(n) — you visit each person once. Dictionary operations and list appends take O(1) amortized time.
Auxiliary space: O(n) — the dictionary temporarily stores people, and ans stores the resulting groups.
Output space: O(n) — every person's index appears exactly once in the answer.
"""