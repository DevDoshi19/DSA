class Node :
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# left -> right -> root
# t.c. whold be O(n) where n is the number of nodes in the tree
# s.c. whold be O(h) where h is the height of the tree

def postorder(node):
    if node is None : 
        return 
    postorder(node.left)
    postorder(node.right)
    print(node.data,end=" -> ")

n1 = Node(5)
n2 = Node(3)
n3 = Node(2)
n4 = Node(9)
n5 = Node(4)
n6 = Node(8)
n7 = Node(1)
n8 = Node(6)
n9 = Node(10)

n1.left = n2
n1.right = n5

n2.left = n3
n2.right = n4

n5.left = n6
n5.right = n9

n6.left = n7
n6.right = n8

postorder(n1)