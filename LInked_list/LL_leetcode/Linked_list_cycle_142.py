# Definition for singly-linked list.

from typing import Optional

class ListNode:
    def __init__(self, x,next = None):
        self.val = x
        self.next = next

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        my_set= set()

        temp = head 
        while temp is not None :
            if temp in my_set:
                return temp
            
            my_set.add(temp)
            temp = temp.next


        return None   # t.c. = O(N) , space = O(n)

class Solution1:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head 

        while fast is not None and fast.next is not None :
            slow = slow.next
            fast = fast.next.next
            if slow == fast :
                slow = head 
                while slow != fast :
                    slow = slow.next
                    fast = fast.next
            
                return slow

        return None

s = Solution1()
s.detectCycle(ListNode(1,(ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))))