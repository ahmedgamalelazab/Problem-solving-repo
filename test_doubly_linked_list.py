
from doubly_linked_list import DoublyLinkedList

def test_initialization_of_dll():
    dll = DoublyLinkedList(10)
    assert dll != None
    assert dll.get_head().data == 10
    
def test_stack_simulation_lifo():
    dll = DoublyLinkedList()
    items_to_push = [10,20,30]
    for item in items_to_push:
        dll.insert_on_tail(item)
    # for lifo we need to chck the tail
    assert dll.get_tail().data == items_to_push[-1]
            

def test_queue_simulation_fifo():
    dll = DoublyLinkedList()
    items_to_queue = [10,20,30]
    for item in items_to_queue:
        dll.insert_on_tail(item)
    assert dll != None
    # for fifo we need to check on head
    assert dll.get_head().data == items_to_queue[0]
    
def test_remove_on_head():
    dll = DoublyLinkedList()
    items = [10,20,30,40]
    for item in items:
        dll.insert_on_head(item)
    dll.remove_from_head()
    assert dll.get_head().data == 30

def test_remove_all_items_from_head_and_check_emptiness():
    dll = DoublyLinkedList()
    items = [10,20,30,40]
    for item in items:
        dll.insert_on_head(item)
    
    for i in range(len(items)):
        dll.remove_from_head()
    
    assert dll.get_head() == dll.get_tail()
    assert dll.get_head() == None
    assert dll.get_tail() == None

def test_remove_all_items_from_tail_and_check_emptiness():
    dll = DoublyLinkedList()
    items = [10,20,30,40]
    for item in items:
        dll.insert_on_tail(item)
    
    for i in range(len(items)):
        dll.remove_from_tail()
    
    assert dll.get_head() == dll.get_tail()
    assert dll.get_head() == None
    assert dll.get_tail() == None
    
    
def test_remove_last_element_using_remove_fn():
    dll = DoublyLinkedList()
    items = [10,20,30,40]
    for item in items:
        dll.insert_on_head(item)
    
    removed = dll.remove(40)
    assert removed == True
    
    assert dll.get_head().data == 30
    
def test_remove_first_element_using_remove_fn():
    dll = DoublyLinkedList()
    items = [10,20,30,40]
    for item in items:
        dll.insert_on_tail(item)
    
    removed = dll.remove(10)
    assert removed == True
    
    assert dll.get_head().data == 20


def test_remove_from_middle_element_using_remove_fn():
    dll = DoublyLinkedList()
    items = [10,20,30,40]
    for item in items:
        dll.insert_on_tail(item)
    
    removed = dll.remove(20)
    assert removed == True
    
    assert dll.get_head().data == 10
    assert dll.get_head().next.data == 30
    assert dll.get_head().next.next.data == 40
    assert dll.get_tail().data == 40


def test_remove_from_and_simulate_clean():
    dll = DoublyLinkedList()
    items = [10,20,30,40]
    for item in items:
        dll.insert_on_tail(item)
    
    remove_results = []
    
    for item in items:
        res = dll.remove(item)        
        remove_results.append(res)
        
    assert dll.get_head() == dll.get_tail() == None
    for rmr in remove_results:
        assert rmr == True
        
        
def test_remove_from_and_simulate_clean_then_try_to_remove():
    dll = DoublyLinkedList()
    items = [10,20,30,40]
    for item in items:
        dll.insert_on_tail(item)
    
    remove_results = []
    
    for item in items:
        res = dll.remove(item)        
        remove_results.append(res)
        
    assert dll.get_head() == dll.get_tail() == None
    for rmr in remove_results:
        assert rmr == True
    
    res = dll.remove(100)
    
    assert res == False
    
    
def test_remove_extra_from_tail():
    dll = DoublyLinkedList()
    dll.insert_on_tail(1)
    dll.insert_on_tail(2)
    
    for i in range(2):
        dll.remove_from_head()
    
    assert dll.remove_from_head() == None
    assert dll.remove_from_tail() == None
    
    dll.insert_on_tail(10)
    dll.insert_on_tail(20)
    
    ri = dll.remove_from_tail()
    assert ri == 20