from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []

        def backtrack(index,path):
            if len(path) > 4 :
                return 
            if index == len(s) and len(path) == 4:
                result.append(".".join(path.copy()))
                return 

            for i in range(index,min(index+3,len(s))):
                n = int(s[index:i+1])
                temp=s[index:i+1]
                if len(temp) >3 :
                    continue
                elif len(temp) > 1 and temp[0] == "0":
                    continue
                elif 0<=n<=255 :
                    path.append(temp)
                    backtrack(i+1,path)

                    path.pop()

        backtrack(0,[])
        return result

# solution 2 : 

class Solution1:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def is_valid(segment):
            if len(segment) > 3 or (len(segment) > 1 and segment[0] == '0'):
                return False
            value = int(segment)
            return 0 <= value <= 255
                
        def backtrack(start, current):
            if len(current) == 4:
                if start == len(s):
                    result.append('.'.join(current))
                return

            for length in range(1, 4):
                if start + length <= len(s):
                    segment = s[start:start+length]
                    if is_valid(segment):
                        current.append(segment)
                        backtrack(start + length, current)
                        current.pop()

        result = []
        backtrack(0, [])
        return result
