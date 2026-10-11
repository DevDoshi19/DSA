from typing import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        new_freq = sorted(freq.items(),key=lambda x:x[1],reverse=True)
        return "".join(key*value for key,value in new_freq)