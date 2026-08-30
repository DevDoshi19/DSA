class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split()
        arr.reverse()
        result = " ".join(arr)
    
        return result
    
class Solution2:
    def reverseWords(self, s: str) -> str:
        arr = s.split()
        newword = []

        for i in range(len(arr)):
            newword.append(arr[len(arr) - 1 - i])

        result = " ".join(newword)
        return result
