class Solution:
    
    def ratInMaze(self, maze):
        n = len(maze)
        result = []
        vis = [[0 for _ in range(n)] for _ in range(n)]

        def findpathHelper(i,j,maze,n,result,move,vis) :
                
            if i == n-1 and j == n -1 :
                result.append(move)
                return 
            
            #down
            if i+1 < n and not vis[i+1][j] and maze[i+1][j] == 1 :
                vis[i][j] = 1
                findpathHelper(i+1,j,maze,n,result,move+"D",vis)
                vis[i][j] = 0
            #left
            if j-1 >= 0  and not vis[i][j-1] and maze[i][j-1] == 1 :
                vis[i][j] = 1
                findpathHelper(i,j-1,maze,n,result,move+"L",vis)
                vis[i][j] = 0
            #Right
            if j+1 < n and not vis[i][j+1] and maze[i][j+1] == 1 :
                vis[i][j] = 1
                findpathHelper(i,j+1,maze,n,result,move+"R",vis)
                vis[i][j] = 0
            #up
            if i-1 >= 0 and not vis[i-1][j] and maze[i-1][j] == 1 :
                vis[i][j] = 1
                findpathHelper(i-1,j,maze,n,result,move+"U",vis)
                vis[i][j] = 0
                
        if maze[0][0] == 1 :
            findpathHelper(0,0,maze,n,result,"",vis)
        
        return result