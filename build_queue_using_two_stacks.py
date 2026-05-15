class MyStack:
    def __init__(self):
        self.stack_list = []
        self.stack_size = 0

    def is_empty(self):
        return self.stack_size == 0

    def peek(self):
        if self.is_empty():
            return None
        return self.stack_list[-1]

    def size(self):
        return self.stack_size
    
    def push(self, value):
        self.stack_size += 1
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        self.stack_size -= 1
        return self.stack_list.pop()
# Push Function => stack.push(int)  //Inserts the element at top
# Pop Function => stack.pop()       //Removes and returns the element at top
# Top/Peek Function => stack.get_top()  //Returns top element
# Helper Functions => stack.is_empty() & stack.isFull() //Returns boolean

class NewQueue:
    def __init__(self):
        self.main_stack = MyStack()


    # Inserts the element in the queue
    def enqueue(self, value):
        self.main_stack.push(value)


    # Removes the element from the queue
    def dequeue(self):
        temp_stack = MyStack()
        for i in range(self.main_stack.size()):
            temp_stack.push(self.main_stack.pop())
        itr = temp_stack.pop()
        for i in range(temp_stack.size()):
            self.main_stack.push(temp_stack.pop())
        return itr



if __name__ == "__main__":
    q = NewQueue()
    
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    
    i = q.dequeue()
    
    print(i)