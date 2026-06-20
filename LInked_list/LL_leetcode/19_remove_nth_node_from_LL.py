# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head 
        length = 0 
        while temp :
            temp = temp.next
            length += 1

        if length == n :
            new_head = head.next
            del head
            return new_head 
        count = length - n
        temp = head

        while count > 1 :
            temp = temp.next
            count -=1 
         
        temp.next = temp.next.next

        return head