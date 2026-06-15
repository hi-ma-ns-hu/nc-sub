class MinStack:

    def __init__(self):
        self.stack = list()
        self.aux_stack = list() # min stack, top item of this stack is always smallest

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.aux_stack or val <= self.aux_stack[-1]:
            self.aux_stack.append(val)

    def pop(self) -> None:
        if self.stack:
            popped = self.stack.pop()
            # if popped is the smallest val, remove it from aux_stack too
            if popped == self.aux_stack[-1]:
                self.aux_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)
