from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five , ten = 0,0

        if bills[0] != 5:
            return False

        for i in range(len(bills)):
            if bills[i] == 5 :
                five +=1
            elif bills[i] == 10 :
                if five > 0:
                    five -=1
                    ten +=1
                else :
                    return False

            elif bills[i] ==20 :
                if ten > 0 and five > 0 :
                    ten -=1
                    five -=1

                elif five >=3 :
                    five -= 3

                else:
                    return False

        return True