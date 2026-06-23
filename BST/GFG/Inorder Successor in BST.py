'''
Definition for Node
'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def inOrderSuccessor(self, root, k):
        self.result = []
        
        def DFS(node):
            if node is None:
                return 
        
            DFS(node.left)
            self.result.append(node.data) 
            DFS(node.right)
            
        DFS(root)
        
        # Find the index of the target node k
        if k.data in self.result:
            ind = self.result.index(k.data)
            if ind + 1 < len(self.result):
                return self.result[ind + 1]
                
        return -1

        
    def solu2(self, root, k):
        self.result = []
        
        succ = -1 
        curr = root 
        while curr :
            
            if k.data < curr.data :
                succ = curr.data
                curr = curr.left
                
            else:
                curr = curr.right
                
            
        return succ