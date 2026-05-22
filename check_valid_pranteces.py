from stack_impl_doubly_linked_list_based import Stack


def check_valid_parentheses(exp: str):
    stack = Stack()
    parentheses_table = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    
    for i in range(len(exp)):
        if stack.is_empty():
            stack.push(exp[i])
            continue
        else:
            if stack.peek() in parentheses_table and parentheses_table[stack.peek()] == exp[i]:
                stack.pop()
            else:
                stack.push(exp[i])
    
    return True if stack.is_empty() else False




if __name__ == "__main__":
    exp = "[{{()}}]"
    output = check_valid_parentheses(exp)
    print(f"The exp {exp} validation result is {output}")