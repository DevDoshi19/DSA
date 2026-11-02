class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        tiles = sorted(list(tiles))
        used = [False] * len(tiles)
        self.count = 0

        def backtrack(path):
            # if len(path) == len(tiles):
            #     return 

            for i in range(0,len(tiles)):
                if i > 0 and tiles[i] == tiles[i-1] and not used[i-1] : # duplicate check, if the current tile is the same as the previous one and the previous one has not been used, we skip this tile to avoid generating duplicate combinations.
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
    
# t.c. = O(n!) in worst case, where n is the length of the tiles string. This is because we are generating all possible permutations of the tiles.
# s.c. = O(n) for the recursion stack and the used array.