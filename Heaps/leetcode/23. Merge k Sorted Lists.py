import heapq
from typing import List, Optional
# Definition for singly-linked list.

"The Pattern — K-way Merge 🧠"
"""
You have K sources
You always want the MINIMUM among K current candidates
→ Use a Min Heap of size K
→ After picking minimum, push the next element from that same source

"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        dummy = ListNode(0)
        curr = dummy

        while heap:
            val, i, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next

            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next
    
"""
Complexity

TimeO(n log k) — n total nodes, k lists in heap
SpaceO(k) — heap stores at most k nodes

Linked List problems

    Merge K Sorted Lists ✅ (just done)
    Merge 2 Sorted Lists (simpler version)

Array problems

    Kth Smallest Element in a Sorted Matrix
    Find K Pairs with Smallest Sums
    Kth Smallest Prime Fraction

Stream problems

    Find Median from Data Stream
    Sliding Window Median

Interval problems

    Meeting Rooms II
    Task Scheduler


- One Line to Remember 💡

"Whenever you have K sorted sources and need the global minimum at each step → Min Heap of size K"

"""

