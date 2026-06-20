class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
        
node1 = Node(5)
node2 = Node(10)
node3 = Node(7)
node4 = Node(8)

node1.next = node2
node2.next = node3
node3.next = node4

print(node1)  # print Address of the value 

print(node1.val)  # print the value 
print(node1.next)  # print Address of the next node
print(node1.next.val)  # print val of the next node
print(node2) 
