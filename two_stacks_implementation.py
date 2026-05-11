class TwoStacks:
    # Initialize the two stacks here
    def __init__(self, size):
        self.stack = [None] * size # a way to simulate fixed size array
        self.stack_1_idx = 0
        self.stack_1_top = 0
        self.stack_2_idx = len(self.stack) -1
        self.stack_2_top = len(self.stack) -1
        
    # Insert Value in First Stack
    def push1(self, value):
        self.stack[self.stack_1_idx] = value
        self.stack_1_idx = self.stack_1_idx + 1
        self.stack_1_top = self.stack_1_idx - 1

    # Insert Value in Second Stack
    def push2(self, value):
        self.stack[self.stack_2_idx] = value
        self.stack_2_idx = self.stack_2_idx - 1
        self.stack_2_top = self.stack_2_idx + 1
        self.stack_2_top = (len(self.stack) -1) if self.stack_2_top >= (len(self.stack) -1) else self.stack_2_top 
        

    # Return and remove top Value from First Stack
    def pop1(self):
        item_to_return = self.stack[self.stack_1_top]
        self.stack[self.stack_1_top] = None
        self.stack_1_top = 0 if self.stack_1_top -1 == 0 else self.stack_1_top -1
        self.stack_1_idx = 0 if self.stack_1_top == 0 else self.stack_1_top + 1
        return item_to_return

    # Return and remove top Value from Second Stack
    def pop2(self):
        item_to_return = self.stack[self.stack_2_top]
        self.stack[self.stack_2_top] = None
        self.stack_2_top = (len(self.stack) -1) if self.stack_2_top == (len(self.stack) -1) else self.stack_2_top + 1  
        self.stack_2_idx = (len(self.stack) -1) if self.stack_2_top == (len(self.stack) -1 ) else self.stack_2_top - 1
        return item_to_return
        
        
        
        
if __name__ == "__main__":
    two_stacks = TwoStacks(5)
    two_stacks.push1(1)
    two_stacks.push1(2)
    two_stacks.push2(3)
    two_stacks.push2(4)
    two_stacks.push2(5)
    two_stacks.push2(6)
    for item in two_stacks.stack:
        print(item)