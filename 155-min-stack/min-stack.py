class MinStack:
    '''
    maintain 2 stacks
    1 keeps track of actual values
    2 keeps track of minimums only
    '''

    def __init__(self):
        self.actual_stack = []
        self.min_stack = []
        
    def push(self, val: int) -> None:
        if not self.actual_stack:
            self.min_stack.append(val)
        else:
            if val < self.min_stack[-1]:
                self.min_stack.append(val)
            else:
                self.min_stack.append(self.min_stack[-1])
        self.actual_stack.append(val)
        return
        
    def pop(self) -> None:
        # if self.actual_stack and self.min_stack and self.actual_stack[-1] == self.min_stack[-1]:
        self.min_stack.pop()
        self.actual_stack.pop()
        return
           

    def top(self) -> int:
        if self.actual_stack:
            return self.actual_stack[-1]

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()