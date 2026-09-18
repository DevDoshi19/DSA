from collections import deque

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: list[str]) -> list[list[str]]:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []
        
        # Phase 1: BFS to find the shortest distance from beginWord to every reachable word
        # mapping: word -> minimum steps from beginWord
        word_steps = {beginWord: 0}
        queue = deque([beginWord])
        found = False
        
        while queue and not found:
            # Process level by level to correctly track depths
            level_size = len(queue)
            current_level_visited = set()
            
            for _ in range(level_size):
                word = queue.popleft()
                
                if word == endWord:
                    found = True
                    break
                
                # Generate all valid 1-letter mutation neighbors
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        next_word = word[:i] + c + word[i+1:]
                        
                        if next_word in wordSet:
                            # If it hasn't been mapped to a step count yet
                            if next_word not in word_steps:
                                word_steps[next_word] = word_steps[word] + 1
                                queue.append(next_word)
                                current_level_visited.add(next_word)
                                
            # Optimization: Remove visited words from wordSet after finishing the level
            # This ensures other paths at the exact same depth can still access them
            for word in current_level_visited:
                wordSet.remove(word)
                
        # If endWord was never reached during BFS, no paths exist
        if endWord not in word_steps:
            return []
        
        # Phase 2: DFS Backtracking from endWord back to beginWord
        results = []
        
        def backtrack(curr_word, current_path):
            if curr_word == beginWord:
                # Since we backtracked from endWord, reverse the final path
                results.append(list(reversed(current_path)))
                return
            
            # Explore neighbors that are exactly 1 step closer to the beginWord
            curr_step = word_steps[curr_word]
            for i in range(len(curr_word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    prev_word = curr_word[:i] + c + curr_word[i+1:]
                    
                    if prev_word in word_steps and word_steps[prev_word] == curr_step - 1:
                        current_path.append(prev_word)
                        backtrack(prev_word, current_path)
                        current_path.pop() # Backtrack step

        # Kickoff DFS starting with the endWord
        backtrack(endWord, [endWord])
        return results


s = Solution()
print(s.findLadders("hit", "cog", ["hot","dot","dog","lot","log","cog"]))