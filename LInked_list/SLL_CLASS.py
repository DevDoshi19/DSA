class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        
class SinglyLinkedList():
    def __init__(self):
        self.head = None
        
    def append(self,value):
        new_node = Node(value)
        
        if self.head == None :
            self.head = new_node
        
        else :
            current_node = self.head
            
            while current_node.next is not None :      # t.c. in worst case is O(N) 
                current_node = current_node.next
                 
            current_node.next = new_node           
            
    def travesal(self):
        if self.head == None :
            print("SLL is Empty")
            
        else :
            current = self.head
            while current is not None :
                print(current.value , end=" ")
                current = current.next
            
        print("\n")
                

    def insert_at_beginning(self,value):           
        if self.head == None:
            self.head = Node(value)
        else :
            new_node = Node(value)
            current_node = self.head
            
            new_node.next = current_node
            self.head = new_node
            
    def insert_at_position(self,value,position):
        new_node = Node(value)
        if self.head == None :
            self.head = new_node
        
        elif position == 0 :
            new_node.next = self.head
            self.head = new_node
        
        else :
            current = self.head
            count = 0 
            prev_node = None      
               
            while current is not None and count < position :
                prev_node = current
                current = current.next
                count += 1 
            
            prev_node.next = new_node
            new_node.next = current
                
    def delete_at_last(self):
        if self.head == None:
            print("Linked List is empty")
        else :
            current = self.head
            while current.next.next is not None :
                current = current.next
                
            current.next = None
                        
    def delete(self,value):
        if self.head == None:
            print("Linked List is empty")
        elif self.head.value == value:
            self.head = self.head.next
        
        else :
            current = self.head 
            prev = None 
            while current.value != value :
                prev = current
                current = current.next 
            
            if current is None:
                print("Value not found")
            else:
                prev.next = current.next
            

sll = SinglyLinkedList()
sll.append(5)
sll.append(10)
sll.append(2)
sll.append(8)

sll.travesal()
sll.insert_at_beginning(1)
sll.travesal()

sll.delete_at_last()
sll.travesal()

sll.insert_at_position(11,2)
sll.travesal()

sll.insert_at_position(100,0)
sll.travesal()

sll.delete_at_last()
sll.travesal()

sll.insert_at_position(19,5)
sll.travesal()

sll.delete(11)
sll.travesal()
sll.delete(100)
sll.travesal()