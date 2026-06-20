# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start = head
        stack = []

        while start is not None :
            stack.append(start.val)
            start = start.next 

        start = head

        while start is not None:
            e = stack.pop()
            start.val = e 
            start = start.next
        
        head = start

        return head 
        

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        prev = None

        while temp is not None :
            front = temp.next 
            temp.next = prev
            prev = temp
            temp = front

        return prev 
    
    
sll = Solution()
reversed_list = sll.reverseList(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))
current = reversed_list