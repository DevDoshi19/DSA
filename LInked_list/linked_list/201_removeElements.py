# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        temp = head

        while temp is not None:

            if temp.val == val:
                prev.next = temp.next

            else:
                prev = temp

            temp = temp.next

        return dummy.next