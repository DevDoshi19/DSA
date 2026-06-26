from collections import deque
from copy import deepcopy
from typing import List

# using BFS
# t.c. O(m*n) s.c. O(m*n)
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])

        pixel = image[sr][sc]
        if pixel == color:
            return image

        image_copy = deepcopy(image)
        image_copy[sr][sc] = color 

        queue = deque()
        queue.append((sr,sc))
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        while len(queue) != 0 :
            r,c = queue.popleft()
            for dr , dc in directions:
                i,j = r+dr , c+dc
                if 0<=i<m and 0<=j<n and image_copy[i][j] == pixel :
                    image_copy[i][j] = color
                    queue.append((i,j))
                  
        return image_copy
    
# using DFS
# t.c. O(m*n) s.c. O(m*n) -> slightly better than BFS as we don't need to maintain a queue
class Solution2:
    def dfs(self,i,j,new_color,pixel,image_copy,r,c):
        if i<0 or i >= r or j<0 or j>= c:
            return
        if image_copy[i][j] == new_color :
            return 
        if image_copy[i][j] != pixel :
            return 
        
        image_copy[i][j] = new_color 
        self.dfs(i-1,j,new_color,pixel,image_copy,r,c)
        self.dfs(i+1,j,new_color,pixel,image_copy,r,c)
        self.dfs(i,j-1,new_color,pixel,image_copy,r,c)
        self.dfs(i,j+1,new_color,pixel,image_copy,r,c)

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])

        pixel = image[sr][sc]
        if pixel == color:
            return image

        image_copy = deepcopy(image)

        self.dfs(sr,sc,color,pixel,image_copy,m,n)

        return image_copy