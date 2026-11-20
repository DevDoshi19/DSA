class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        ans = []
        n = len(s)
        worddict = set(wordDict)
        def solve(index,lst):
            if index >= n :
                ans.append(" ".join(lst.copy()))
                return 

            for end in range(index+1,n+1):
                new_s = s[index:end]
                if new_s not in worddict :
                    continue

                lst.append(new_s)
                solve(end,lst)
                lst.pop()

        solve(0,[])
        return ans