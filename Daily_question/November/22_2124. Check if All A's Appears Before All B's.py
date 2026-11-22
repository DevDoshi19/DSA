class Solution:
    def checkString(self, s: str) -> bool:
        # isB = False 
        # for i in s :
        #     if i == "a" and isB == True :
        #         return False
        #     if i == "b":
        #         isB = True 

        # return True

        for i in range(len(s)-1):
            if s[i] == "b" and s[i+1] =="a":
                return False

        return True 