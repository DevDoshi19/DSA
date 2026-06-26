from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        time = 0 
        
        # We need a loop that keeps running minute-by-minute
        while True:
            # This flag tracks if any fresh orange rots during this minute
            rotted_this_minute = False
            
            # We must create a temporary snapshot of the grid at the start of this minute.
            # This prevents an orange that rots *now* from rotting its neighbor *in the same minute*.
            prev_grid = [row[:] for row in grid]
            
            for i in range(m):
                for j in range(n):
                    # We check the snapshot (prev_grid) to see what was already rotten
                    if prev_grid[i][j] == 2:
                        
                        # 1. Check UP neighbor: (i-1, j)
                        if i > 0 and grid[i-1][j] == 1:
                            grid[i-1][j] = 2 # Corrected: Turn to 2 (rotten), not 1
                            rotted_this_minute = True
                            
                        # 2. Check DOWN neighbor: (i+1, j)
                        if i + 1 < m and grid[i+1][j] == 1:
                            grid[i+1][j] = 2
                            rotted_this_minute = True
                            
                        # 3. Check LEFT neighbor: (i, j-1)
                        if j > 0 and grid[i][j-1] == 1:
                            grid[i][j-1] = 2
                            rotted_this_minute = True
                            
                        # 4. Check RIGHT neighbor: (i, j+1)
                        if j + 1 < n and grid[i][j+1] == 1:
                            grid[i][j+1] = 2
                            rotted_this_minute = True
            
            # If no oranges rotted during this entire grid scan, stop the time
            if not rotted_this_minute:
                break
                
            time += 1
            
        # Final scan to see if any fresh orange (1) is left untouched
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1 # Return integer -1, not string "-1"
                    
        return time
