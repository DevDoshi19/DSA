# level order traversal of a binary tree

from typing import Deque


class Node :
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# the time complexity of this algorithm is O(n) where n is the number of nodes in the tree
# the space complexity of this algorithm is O(n) where n is the number of nodes in

# working of the algorithm is as follows :
# 1. we create a queue and add the root node to it
# 2. we pop the first element from the queue and add its left and right children
# 3. we repeat step 2 until the queue is empty

"""
example : dry run of the algorithm on the following tree :
queue : []

queue : [1]        ,    result : []
queue : [2,3]      ,    result : [1]
queue : [3,4,5]    ,    result : [1,2]
queue : [4,5,6,7]  ,    result : [1,2,3]
queue : [5,6,7]    ,    result : [1,2,3,4]
queue : [6,7]      ,    result : [1,2,3,4,5]
queue : [7]        ,    result : [1,2,3,4,5,6]
queue : []         ,    result : [1,2,3,4,5,6,7]

"""

def BFS(node):
    result = []
    queue = Deque()
    queue.append(node)

    while len(queue) != 0:
        e = queue.popleft()
        result.append(e.data)
        if e.left is not None :
            queue.append(e.left)
        if e.right is not None :
            queue.append(e.right)

    return result 

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n8 = Node(8)
n9 = Node(9)
n10 = Node(10)

n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7
n4.left = n8
n5.right = n9
n6.left = n10
ans = BFS(n1)
print(ans)