class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insert_at_head(self, val):
        new_node = Node(val)
        if self.head == None :
            self.head = new_node
            self.tail = new_node      
        else :
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            
    def append(self,val):
        new_node = Node(val)
        if self.head == None :
            self.head = new_node
            self.tail = new_node
        else :
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node    
            
    def display(self):
        current = self.head
        while current is not None :
            print(current.val,end=" <-> ")
            current = current.next
        print("\n")
            
    def insert_at_position(self, pos, val):
        new_node = Node(val)
        if pos == 0 :
            self.insert_at_head(val)
        else :
            current = self.head
            count = 0
            while current is not None and count < pos-1 :
                current = current.next
                count += 1
            if current is None :
                print("Position out of bounds")
            else :
                new_node.next = current.next
                new_node.prev = current
                if current.next is not None :
                    current.next.prev = new_node
                current.next = new_node
                if new_node.next is None :
                    self.tail = new_node
    
    def delete_head(self):
        if self.head == None :
            print("List is empty")
        else :
            self.head = self.head.next
            self.head.prev = None
    
    def delete_tail(self):
        if self.tail == None :
            print("List is empty")
        else :
            self.tail = self.tail.prev
            self.tail.next = None
            
    def delete_at_position(self, pos):
        if self.head is None:
            print("List is empty")
        elif pos == 0:
            self.delete_head()
        else:
            current = self.head 
            count = 0
            while current is not None and count < pos-1:
                current = current.next
                count += 1
            
            if current is None:
                print("Position out of bounds")
                
            current.next.prev = current
            current.prev.next = current.next
            if current.next is None:
                self.tail = current.prev
            if current.prev is None:
                self.head = current.next    
            
dll = DoublyLinkedList()
dll.insert_at_head(10)
dll.insert_at_head(5)
dll.append(20)
dll.insert_at_head(1)
dll.append(30)
dll.append(31)
dll.append(32)
dll.append(33)
dll.append(34)
dll.append(35)
dll.append(36)
dll.append(37)
dll.append(38)
dll.append(39)
dll.append(40)
dll.display()
dll.delete_tail()
dll.delete_head()
dll.delete_at_position(6)
dll.display()
