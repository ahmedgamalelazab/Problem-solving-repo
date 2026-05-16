
from doubly_linked_list import DoublyLinkedList


class Stack:
    def __init__(self):
        self.lst = DoublyLinkedList()
        self.size = 0
    
    def push(self, item):
        self.lst.insert_on_tail(item)
    
    def pop(self):
        return self.lst.remove_from_tail()
        
    def peek(self):
        return self.lst.get_tail().data if self.lst.get_tail() else -1
    