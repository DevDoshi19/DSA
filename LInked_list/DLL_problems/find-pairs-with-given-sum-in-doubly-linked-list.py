from typing import Optional


from typing import List


# Definition for singly Link List Node
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None
        self.prev=None

"""
You can also use the following for printing the link list.
displayList(node)
"""

class Solution:
    def findPairsWithGivenSum(self, target : int, head : Optional['Node']) -> List[List[int]]:
        # code here
        
        left = head
        right = head 
        result = []
        
        while right.next :
            right = right.next
            
        while left is not None and right is not None and left.data <right.data:
            value = left.data + right.data
            
            if value > target :
                right = right.prev
            elif value == target:
                result.append([left.data,right.data])
                left = left.next
                right = right.prev
                
            else:
                left =left.next
                
        return result 
    
    
# we can also use set if the list is not sorted and we have to find the pairs with given sum in unsorted doubly linked list.
# which give use O(n) time complexity and O(n) space complexity. because we have to store the values in set and then check for the pairs.


# this approch is only for sorted doubly linked list. because we are using two pointer approach. if the list is not sorted then we have to sort the list first and then apply two pointer approach which will give us O(nlogn) time complexity.
# t.c. : O(n) and s.c. : O(1) for sorted list.