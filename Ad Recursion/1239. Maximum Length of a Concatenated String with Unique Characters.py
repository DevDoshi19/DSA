class Solution:
    def maxLength(self, arr: list[str]) -> int:
        n =len(arr)
        self.maxi = 0

        def backtrack(index,temp):
            self.maxi = max(self.maxi,len(temp))

            if index == n :
                return 

            for i in range(index,n) :
                curr = temp
                candidate = arr[i]
                if len(set(candidate)) != len(candidate) :
                    continue

                valid = True
                for c in candidate :
                    if c in temp :
                        valid = False
                        break

                if not valid:
                    continue

                temp += candidate
                backtrack(i+1,temp)
                temp = curr
                            
        backtrack(0,"")
        return self.maxi