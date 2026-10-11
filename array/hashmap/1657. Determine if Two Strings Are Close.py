from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        n = len(word1)
        m = len(word2)
        if n != m :
            return False

        freq1 = Counter(word1)
        freq2 = Counter(word2)

        if set(freq1) != set(freq2):
            return False
        
        sorted_freq1 = sorted(freq1.values())
        sorted_freq2 = sorted(freq2.values())

        return sorted_freq1 == sorted_freq2