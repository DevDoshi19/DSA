class Node:
    def __init__(self,val):
        self.val = val
        self.prev = None
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self,val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def pop(self):
        if not self.tail:
            return None
        val = self.tail.val
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return val

    def top(self):
        if not self.tail:
            return None
        return self.tail.val

    def is_empty(self):
        return self.head is None

# Example usage:
stack = Stack()
stack.push(1)
stack.push(2)
print(stack.top())  # Output: 2
print(stack.pop())  # Output: 2
print(stack.top())  # Output: 1
print(stack.is_empty())  # Output: False
