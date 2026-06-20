from typing import List
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        letter = []

        for i in range(len(s)):

            if s[i].isalpha():
                letter.append(i)

        k = len(letter)

        total = 1 << k

        result = []

        for mask in range(total):

            temp = list(s)

            for j in range(k):

                index = letter[j]

                if mask & (1 << j):

                    temp[index] = temp[index].upper()

                else:

                    temp[index] = temp[index].lower()

            result.append("".join(temp))

        return result