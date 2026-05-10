'''
Stack implementation
'''

class MissingContainerStackProperty(Exception):
    def __init__(self, *args):
        super().__init__(*args)

# Acceptance policies for the dynamic container

ABSTRACTED_METHOD_EXCEPTION_MESSAGE = "Property Not Implemented!"

class IContainerViolationPolicy:
    def apply(self, container):
        raise Exception(ABSTRACTED_METHOD_EXCEPTION_MESSAGE)

class MissingPushPropertyOnContainerPolicy(IContainerViolationPolicy):
    def apply(self, container):
        if not hasattr(container, "push"):
            raise MissingContainerStackProperty("Push property not exists on the given container")

class MissingPopPropertyOnContainerPolicy(IContainerViolationPolicy):
    def apply(self, container):
        if not hasattr(container, "pop"):
            raise MissingContainerStackProperty("Pop property not exists on the given container")

# abstract class
class IStack:
    def __init__(self, dynamic_container):
        self._dynamic_container = dynamic_container
        self._container_policies: list[IContainerViolationPolicy] = [MissingPushPropertyOnContainerPolicy(), MissingPopPropertyOnContainerPolicy()]
        for policy in self._container_policies:
            policy.apply(self._dynamic_container)
    
    def push(self, element):
        raise Exception(ABSTRACTED_METHOD_EXCEPTION_MESSAGE) 
    
    def pop(self):
        raise Exception(ABSTRACTED_METHOD_EXCEPTION_MESSAGE) 
    
    def peek(self):
        raise Exception(ABSTRACTED_METHOD_EXCEPTION_MESSAGE) 
    
    def is_empty(self)-> bool:
        raise Exception(ABSTRACTED_METHOD_EXCEPTION_MESSAGE) 
    
    def size(self) -> int:
        raise Exception(ABSTRACTED_METHOD_EXCEPTION_MESSAGE)
    
    
class StackContainer:
    def __init__(self):
        self.lst = []
    
    def push(self, element):
        self.lst.append(element)
    
    def pop(self):
        return self.lst.pop()
    
    
class StackImplV1(IStack):
    def __init__(self, dynamic_container):
        super().__init__(dynamic_container)
        self._size = 0
    
    def push(self, element):
        self._dynamic_container.push(element)
        self._size = self._size + 1
    
    def pop(self):
        if not self.is_empty():
            self._size = self._size -1
            return self._dynamic_container.pop() 
        else:
            return None
        
    def peek(self):
        return self._dynamic_container.lst[-1]
    
    def is_empty(self)-> bool:
        return True if self._size == 0 else False
    
    def size(self) -> int:
        return self._size
    
    
    
if __name__ == "__main__":
    stack = StackImplV1(StackContainer())
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    
    print(stack.peek())
    
    print(stack.size())
    
    print("pooping one element", stack.pop())
    print("pooping one element", stack.pop())
    print("pooping one element", stack.pop())
    print("pooping one element", stack.pop())
    print("pooping one element", stack.pop())
    print("pooping one element", stack.pop())
    print("pooping one element", stack.pop())
    print("pooping one element", stack.pop())
    
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    
    print(stack.peek())