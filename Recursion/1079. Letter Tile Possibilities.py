class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        tiles = sorted(list(tiles))
        used = [False] * len(tiles)
        self.count = 0

        def backtrack(path):
            if len(path) == len(tiles):
                return 

            for i in range(0,len(tiles)):
                if i > 0 and tiles[i] == tiles[i-1] and not used[i-1] :
                    continue
                elif used[i] :
                    continue
                
                self.count += 1
                used[i] = True
                path.append(tiles[i])
                backtrack(path)
                path.pop()
                used[i] = False
                
        backtrack([])
        return self.count