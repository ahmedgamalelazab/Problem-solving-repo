class TwoStacks:
    def __init__(self, n):  
        self.size = n
        self.arr = [0] * n  
        self.top1 = -1
        self.top2 = self.size

    def push1(self, value):
        # Increment top pointer and add element to stack 1 if space is available, else print stack overflow and exit
        if self.top1 < self.top2 - 1:
            self.top1 += 1
            self.arr[self.top1] = value
        else:
            print("Stack Overflow ")
            exit(1)

    def push2(self, value):
        # Decrement top pointer and add element to stack 2 if space is available, else print stack overflow and exit
        if self.top1 < self.top2 - 1:
            self.top2 -= 1
            self.arr[self.top2] = value
        else:
            print("Stack Overflow ")
            exit(1)

    def pop1(self):
        # Return and remove top element from stack 1 if not empty, else print stack underflow and exit
        if self.top1 >= 0:
            value = self.arr[self.top1]
            self.top1 -= 1
            return value
        else:
            print("Stack Underflow ")
            exit(1)

    def pop2(self):
        # Return and remove top element from stack 2 if not empty, else print stack underflow and exit
        if self.top2 < self.size:
            value = self.arr[self.top2]
            self.top2 += 1
            return value
        else:
            print("Stack Underflow ")
            exit()
def main():
    calls = [
        ["TwoStacks", "push1", "push2", "pop2"],
        ["TwoStacks", "push1", "pop1", "push2", "pop2"],  
        ["TwoStacks", "push1", "push2", "push1", "push2", "pop1", "pop2", "pop1"],      
        ["TwoStacks", "push2", "pop2", "push2", "push1"],
        ["TwoStacks", "push1", "push1", "push2", "pop1"],
    ]

    inputs = [
        [5, 10, 15, None],
        [7, -4, None, -6, None],
        [5, 10, 20, 50, 30, None, None, None],
        [10, 4, None, 8, 10],
        [3, 10, 20, 30, None],
    ]

    for i in range(len(calls)):
        print(f"Testcase {i + 1}:")
        stack_obj = TwoStacks(inputs[i][0])

        for j in range(1, len(calls[i])):
            if calls[i][j] == "push1":
                stack_obj.push1(inputs[i][j])
            elif calls[i][j] == "push2":
                stack_obj.push2(inputs[i][j])
            elif calls[i][j] == "pop1":
                print(f"\tpop1 returns {stack_obj.pop1()}")
            elif calls[i][j] == "pop2":
                print(f"\tpop2 returns {stack_obj.pop2()}")

        print("-" * 50)


if __name__ == "__main__":
    main()