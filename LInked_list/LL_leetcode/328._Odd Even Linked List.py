# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        
        if temp is None or temp.next is None:
            return head
        
        my_list = []
        while temp :
            my_list.append(temp.val)
            temp = temp.next.next if temp.next else None

        temp = head.next

        while temp :
            my_list.append(temp.val)
            temp = temp.next.next if temp.next else None

        temp = head
        i = 0
        while temp is not None :
            temp.val = my_list[i]
            i+=1
            temp = temp.next

        return head

