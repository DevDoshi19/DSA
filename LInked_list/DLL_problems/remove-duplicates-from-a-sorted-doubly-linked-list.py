class Node:
    def __init__(self, value):
        self.data = value  # value stored in node
        self.next = None
        self.prev = None

class Solution:
    def removeDuplicates(self, headRef):
        # code here
        current = headRef 
        while current is not None and current.next is not None :
            if current.data == current.next.data:
                current.next = current.next.next
                if current.next != None:
                    current.next.prev = current
            
            else :
                current = current.next
            
            
        return headRef