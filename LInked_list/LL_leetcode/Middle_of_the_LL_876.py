from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Brute Force Approach

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        self.head = head
        current = self.head
        count = 0 
        while current is not None :
            current = current.next 
            count += 1

        current = self.head

        for _ in range(count//2):       
            current = current.next 

        return current
    
    
sll = Solution()
middle_node = sll.middleNode(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))
# print(middle_node.val)  # Output: 3


# Optimal Approach (Floyd's Tortoise and Hare Algorithm)

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        fast = head
        slow = head
        
        while fast is not None and fast.next is not None :
            slow = slow.next
            fast = fast.next.next 
 
        return slow