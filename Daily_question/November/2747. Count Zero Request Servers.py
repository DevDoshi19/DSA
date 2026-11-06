from typing import List

# brute force solution
class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        ans = []
        
        logs.sort(key=lambda x:x[1])
        for q in queries:
            server = set()
            x1,x2 = q-x , q
            for i ,j in logs:
                if x1 <= j <= x2 :
                    server.add(i) 
                
            ans.append(n-len(server)) 
        
        return ans


class Solution2:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        # sliding window approach

        m = len(logs)
        logs.sort(key=lambda x:x[1]) # t.c. = O(mlogm)

        sorted_queries = sorted((q, i) for i, q in enumerate(queries))  # t.c. = O(qlogq)

        mp = {}
        q = len(queries)
        ans = [0] * q
        i,j= 0,0
        
        for time, index in sorted_queries : # t.c. = O(q + 2m)
            start ,end = time - x , time 
            while j < m and logs[j][1] <= end :
                mp[logs[j][0]] = mp.get(logs[j][0],0)+1
                j += 1

            while i < m and logs[i][1] < start :
                mp[logs[i][0]] -= 1
                if mp[logs[i][0]] == 0 :
                    del mp[logs[i][0]]
                i += 1

            ans[index] = n - len(mp) 

        return ans