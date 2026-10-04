#t.c. = O(n) , s.c. = O(n)
class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split()
        arr.reverse()
        result = " ".join(arr)
    
        return result

# t.c. = O(n) , s.c. = O(n)   
class Solution2:
    def reverseWords(self, s: str) -> str:
        arr = s.split()
        newword = []

        for i in range(len(arr)):
            newword.append(arr[len(arr) - 1 - i])

        result = " ".join(newword)
        return result

# manual approach without using split  
# t.c. = O(n) , s.c. = O(n)
class Solution3:
    def reverseWords(self, s: str) -> str:
        newword = []
        word =""
        for i in s:
            if i != " ":
                word += i
            else:
                if word:
                    newword.append(word)
                    word =""
        if word:
            newword.append(word)
    
        return " ".join(newword[::-1])
