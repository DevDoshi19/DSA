from collections import defaultdict, deque

class Solution:
    def numMatchingSubseq(self, s: str, words: list[str]) -> int:

        waiting = defaultdict(deque)

        # Put every word into the bucket corresponding to its first character, which is form word
        for word in words:
            waiting[word[0]].append((word, 0))

        count = 0

        # Scan s only once
        for ch in s:
            current = waiting[ch] # Process everyone waiting for this character
            size = len(current)

            for _ in range(size):
                word, index = current.popleft()

                index += 1
                if index == len(word): # Word completely matched
                    count += 1

                else:
                    # Wait for the next character
                    next_ch = word[index]
                    waiting[next_ch].append((word, index))

        return count