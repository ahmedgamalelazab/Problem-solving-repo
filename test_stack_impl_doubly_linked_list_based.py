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