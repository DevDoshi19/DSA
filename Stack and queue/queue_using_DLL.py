class Node:
    def __init__(self,val):
        self.val = val
        self.prev = None
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def enqueue(self,val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        
        else :
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if not self.head:
            return None
        val = self.head.val
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return val

    def front(self):
        if not self.head:
            return None
        return self.head.val

    def is_empty(self):
        return self.head is None
    
# Example usage:
queue = Queue()     
queue.enqueue(1)
queue.enqueue(2)    
print(queue.front())  # Output: 1
print(queue.dequeue())  # Output: 1
print(queue.front())  # Output: 2
print(queue.is_empty())  # Output: False
