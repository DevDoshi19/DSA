class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        r = len(board)
        c = len(board[0])
        self.isExist = False        
        visited = [[False for _ in range(c)] for _ in range(r)]

        def dfs(board,row,col,word_index,visited):
            if word_index == len(word):
                return True

            if row < 0 or row >= r or col < 0 or col >= c:
                return False
            
            if word[word_index] != board[row][col]:
                return False
            if visited[row][col]:
                return False
            
            visited[row][col] = True

            found = (dfs(board,row,col+1,word_index+1,visited) or
            dfs(board,row,col-1,word_index+1,visited) or
            dfs(board,row+1,col,word_index+1,visited) or
            dfs(board,row-1,col,word_index+1,visited))
            
            visited[row][col] = False

            return found

        for i in range(0,r):
            for j in range(0,c):
                if dfs(board,i,j,0,visited):
                    self.isExist = True

        
        return self.isExist

# the t.c. = O(R*C * 3*L) where R is the number of rows, C is the number of columns, and L is the length of the word. The 3^L factor arises because from each cell, we can explore up to 3 directions (excluding the direction we came from) for each character in the word.
# the s.c. = O(R*C) for the visited array and O(L) for the recursion stack, where L is the length of the word.