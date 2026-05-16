
from doubly_linked_list import DoublyLinkedList


class Stack:
    def __init__(self):
        self.lst = DoublyLinkedList()
        self.size = 0
    
    def push(self, item):
        self.lst.insert_on_tail(item)
        self.size = self.size + 1
    
    def pop(self):
        if self.is_empty():
            return None
        self.size = self.size - 1
        return self.lst.remove_from_tail()
        
    def peek(self):
        return self.lst.get_tail().data if self.lst.get_tail() else None
    
    def is_empty(self):
        return True if self.size == 0 else False