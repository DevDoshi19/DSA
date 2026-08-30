
from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        ans = []
        sortfreq = dict(sorted(freq.items(),key=lambda item: item[1] ,reverse= True))
        for char, count in sortfreq.items():
            ans.append(char*count)

        return "".join(ans)
            

# this is using the built-in function most_common() of the Counter class to sort the characters by frequency in descending order. It then constructs the final string by repeating each character according to its frequency and joining them together.
class Solution2:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        return "".join(char*count for char,count in freq.most_common())
            