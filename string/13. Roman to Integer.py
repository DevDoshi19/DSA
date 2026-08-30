class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0 
        dic = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
        }

        for i in range(len(s)) :  
            ans += dic[s[i]] 
            # the 2 * dic[s[i-1]] is subtracted because we have already added the value of the previous character to the total, but since it is smaller than the current character, we need to subtract it twice to account for the fact that it was added once and should not be counted at all in this case.
            if i> 0 and i <len(s) and dic[s[i-1]] < dic[s[i]] :
                ans -=  2* dic[s[i-1]]
            

        return ans
    
class Solution2:
    def romanToInt(self, s: str) -> int:
        ans = 0 
        dic = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
        }
        # forward iteration through the string, checking if the current character is greater than the previous character. If it is, we subtract twice the value of the previous character from the total to account for the fact that it was added once and should not be counted at all in this case. Otherwise, we simply add the value of the current character to the total.
        for i in range(len(s)) :  
            if i> 0 and i <len(s) and dic[s[i-1]] < dic[s[i]] :
                ans += dic[s[i]] - 2* dic[s[i-1]]
            else :
                ans += dic[s[i]] 
            

        return ans
    
class solution3:
    def romanToInt(self, s: str) -> int:
        ans = 0 
        dic = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
        }
        # backward iteration through the string, checking if the current character is less than the next character. If it is, we subtract the value of the current character from the total to account for the fact that it should not be counted at all in this case. Otherwise, we simply add the value of the current character to the total.
        for i in range(len(s)-1,-1,-1) :  
            if i < len(s)-1 and dic[s[i]] < dic[s[i+1]] :
                ans -= dic[s[i]]
            else :
                ans += dic[s[i]] 
            

        return ans