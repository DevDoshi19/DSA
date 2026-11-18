class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        self.maxi = 0
        n = len(s)

        def solve(index,split,lookup):
            if index >= n :
                self.maxi = max(self.maxi,split)
                return 

            for i in range(index+1,n+1):
                temp = s[index:i]
                if temp in lookup :
                    continue

                lookup.append(temp)
                solve(i,split+1,lookup)
                lookup.pop()

        solve(0,0,[])
        return self.maxi
    
    # t.c. = O(2^n * n**2)  temp in lookup takes up to O(n) comparisons, and each string comparison can itself take up to O(n) time.
    # and s.c. = O(n)