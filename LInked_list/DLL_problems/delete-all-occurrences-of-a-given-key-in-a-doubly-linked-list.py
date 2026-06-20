
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
class Solution:
    
    # Function to delete all occurrences of x
    def deleteAllOccurOfX(self, head, x):
        # code here
        
        if head.next is None and head.data == x :
            return None
        
        prev = None 
        temp = head
        new_head = head
        
        while temp is not None:
            
            if temp.data == x :
                if prev is not None :    
                    prev.next = temp.next
                if temp.next is not None:
                    temp.next.prev = prev
                if temp == new_head :
                    new_head = new_head.next 
            
            prev = temp 
            temp = temp.next 
                
        return new_head 