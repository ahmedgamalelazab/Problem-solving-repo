from stack_impl_doubly_linked_list_based import Stack



def test_simple_stack_impl():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    
    assert stack.peek() == 4
    ri = stack.pop()
    assert ri == 4
    
    assert stack.peek() == 3
    ri = stack.pop()
    assert ri == 3
    
def test_size_tracking_of_stack():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    
    ri = stack.pop()
    assert ri == 2
    assert stack.peek() == 1
    ri = stack.pop()
    assert ri == 1
    assert stack.peek() == None
    ri = stack.pop()
    assert ri == None
    stack.push(30)
    assert stack.peek() == 30