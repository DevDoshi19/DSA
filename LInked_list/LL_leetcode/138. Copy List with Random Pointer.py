"""
# Definition for a Node.
"""
from typing import Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None :
            return None 
        
        hashmap = {}

        temp = head 

        while temp:
            hashmap[temp] = Node(temp.val)
            temp = temp.next

        temp = head
        while temp :
            if temp.next :
                hashmap[temp].next = hashmap[temp.next]
            if temp.random :
                hashmap[temp].random = hashmap[temp.random]
            temp = temp.next

        return hashmap[head]