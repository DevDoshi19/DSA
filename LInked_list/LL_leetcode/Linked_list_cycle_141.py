# Definition for singly-linked list.

from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        my_set= set()

        temp = head 
        while temp is not None :
            if temp in my_set:
                return True
            
            my_set.add(temp)
            temp = temp.next


        return False   # t.c. = O(N) , space = O(n)
    
    
# This is the optimal solution using the Floyd's Tortoise and Hare algorithm (two pointers approach) with O(1) space complexity and O(N) time complexity.

class Solution1:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False
        
        slow = head
        fast = head

        while fast is not None and fast.next is not None :
            slow = slow.next
            fast = fast.next.next

            if fast == slow :
                return True

        return False

        