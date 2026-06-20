'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def findMaxFork(self, root, k):
        #code here
        curr = root 
        floor = -1
        while curr :
            if curr.data == k :
                return curr.data
                
            if curr.data > k :
                curr = curr.left
                
            elif curr.data < k :
              floor = curr.data
              curr = curr.right 
              
        return floor