# Doubly linked list implementation
class Node:
    def __init__(self, data, next, prev):
        self.data = None if data == None else data
        self.next = None if next == None else next
        self.prev = None if prev == None else prev
        
        
class DoublyLinkedList:
    def __init__(self, initial_data = None):
        self.head = self.tail = Node(initial_data, None, None) if initial_data else None
        
    def get_head(self):
        return self.head

    def get_tail(self):
        return self.tail
    
    def insert_on_head(self, data):
        if self.head == self.tail and self.head == None:
            self.head = self.tail = Node(data, None, None)
        else:
            head_ptr = self.head
            self.head = Node(data, self.head, None)
            head_ptr.prev = self.head
            head_ptr = None
    
    def insert_on_tail(self, data):
        if self.tail == self.head and self.tail == None:
            self.head = self.tail = Node(data, None, None)
        else:
            tail_ptr = self.tail
            self.tail = Node(data, None, tail_ptr)
            tail_ptr.next = self.tail
            tail_ptr = None
        
    def remove_from_head(self):
        if self.head == self.tail == None:
            return None
        
        if (self.head == self.tail) and (self.head or self.tail):
            rd = self.head.data
            self.head = self.tail = None
            return rd
        else:
            head_ptr = self.head
            self.head = self.head.next
            rd = head_ptr.data
            self.head.prev = None
            head_ptr.next = None
            head_ptr = None
            return rd
    
    def remove_from_tail(self):
        if self.head == self.tail == None:
            return None
        
        if (self.head == self.tail) and (self.head or self.tail):
            rd = self.head.data
            self.head = self.tail = None
            return rd
        else:
            tail_ptr = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            rd = tail_ptr.data
            tail_ptr.prev = None
            tail_ptr = None
            return rd
    
    def remove(self, data):
        if self.head == self.tail and self.head == None:
            return False
        else:
            head_ptr = self.head
            found_node = None
            while head_ptr != None:
                if head_ptr.data == data:
                    found_node = head_ptr
                    break
                else:
                    head_ptr = head_ptr.next
            
            if found_node:
                found_ptr = found_node
                if found_ptr.prev == found_ptr.next and found_ptr.next == None:
                    self.head = self.tail = None
                    found_ptr = None
                    found_node = None
                    return True
                else:
                    if found_ptr:
                        if self.head == found_ptr:
                            self.head = self.head.next
                            self.head.prev = None
                        if self.tail == found_ptr:
                            self.tail = self.tail.prev
                            self.tail.next = None
                        if found_ptr.prev:
                            found_ptr.prev.next = found_ptr.next if found_ptr.next else None
                        if found_ptr.next:
                            found_ptr.next.prev = found_ptr.prev if found_ptr.prev else None
                        found_node.next = None
                        found_node.prev = None
                        found_node = None
                        found_ptr = None
                        return True     
            else:
                return False                
    
    def insert(self, idx, data):
        raise Exception("Method Not implemented yet")        