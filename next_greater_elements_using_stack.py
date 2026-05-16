from stack_impl_doubly_linked_list_based import Stack



def generate_next_greater_element(lst: list[int])-> list[int]:
    stack = Stack()
    res = [-1] * len(lst)
    
    # traverse in reverse order
    for i in range((len(lst) -1), -1, -1):
        while not stack.is_empty() and stack.peek() <= lst[i]:
            stack.pop()
        
        if not stack.is_empty():
            res[i] = stack.peek()
                
        stack.push(lst[i])
    
    return res



if __name__ == "__main__":
    lst_for_expermental = [3,10,6,11,1,1,13,9,17,1]
    output = generate_next_greater_element(lst_for_expermental)
    print(output)