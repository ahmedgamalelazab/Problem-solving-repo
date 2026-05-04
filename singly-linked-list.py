# We write our own singly linked list


class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class SinglyLinkedList:
    def __init__(self, initial_value):
        if initial_value != None:
            self.head = Node(initial_value, None)
        else:
            self.head = None
    
    def get_head(self):
        return self.head
    
    def insert_at_tail(self, data):
        traversal_ptr = self.head
        if traversal_ptr == None:
            traversal_ptr = Node(data, None)
            return None
        else:
            while traversal_ptr.next != None:
                traversal_ptr = traversal_ptr.next
            
            traversal_ptr.next = Node(data, None)
            return None

    def insert_at_head(self, data):
        traversal_ptr = self.head
        if traversal_ptr == None:
            traversal_ptr = Node(data, None)
            return None
        else:
            traversal_ptr.next = self.head.next
            self.head = Node(data, traversal_ptr)
            return None
    
    def _delete(self, prev, curr, data):
        # base case
        if curr == None:
            return False
        if curr.data == data:
            if prev == None:
                temp = curr
                curr = curr.next
                self.head = curr
                temp.next = None
                return True
            else:
                prev.next = curr.next
                curr.next = None
                return True
        else:
            return self._delete(curr, curr.next, data)
    
    def delete(self, data):
        return self._delete(None, self.head, data)
    
    def delete_at_head(self):
        if self.head == None:
            return None
        else:
            traversal_ptr = self.head.next
            self.head.next = None
            self.head = traversal_ptr
            return None
    
    def search(self, data):
        if self.head == None:
            return -1
        else:
            traversal_ptr = self.head
            while traversal_ptr != None:
                if traversal_ptr.data == data:
                    return data
                else:
                    traversal_ptr = traversal_ptr.next
            return -1
    
    def is_empty(self):
        if self.head == None:
            return True
        else:
            return False
    
    def print_self(self):
        traversal_ptr = self.head
        while traversal_ptr != None:
            print(traversal_ptr.data)
            traversal_ptr = traversal_ptr.next    
        
        
        
if __name__ == "__main__":
    linked_list = SinglyLinkedList(10)
    linked_list.insert_at_tail(20)
    linked_list.insert_at_tail(30)
    linked_list.insert_at_tail(40)
    linked_list.insert_at_tail(50)
    linked_list.print_self()
    # linked_list.delete_at_head()
    # linked_list.print_self()
    print("=================================")
    linked_list.delete(30)
    linked_list.delete(50)
    linked_list.delete(20)
    linked_list.delete(10)
    linked_list.print_self()
    
    