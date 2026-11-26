class Solution:
    def canAliceWin(self, n: int) -> bool: 
        # value = 10 
        # isAliceWin = False
        # for i in range(10):
        #     if n - value == 0 :
        #         if i % 2 == 0:
        #             isAliceWin = True
        #         return isAliceWin
        #     elif (n - value) < 0 :
        #         if i % 2 != 0:
        #             isAliceWin = True
        #         return isAliceWin

        #     n = n - value
        #     value -= 1
        #     isAliceWin = False

        # return False 
        value = 10
        for i in range(10):
            if n < value:
                return i % 2 != 0

            n -= value

            if n == 0:
                return i % 2 == 0

            value -= 1

        return False