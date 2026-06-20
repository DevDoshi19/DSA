
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None

class Solution:
    def reverse(self, head):
        # code here
        if head.next is None and head.prev is None :
            return head
        
        prev = None 
        front = head
        temp = head 
        
        while temp is not None :
           
            front = front.next
            temp.next = prev 
            temp.prev = front
            prev = temp 
            temp = front
        
        return prev 