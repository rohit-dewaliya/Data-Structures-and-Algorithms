class MyQueue:
    def __init__(self):
        self.stack = []
        self.len = 0

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.len += 1

    def pop(self) -> int:
        temp_stack = []
        if not self.empty():
            while self.stack:
                temp_stack.append(self.stack.pop())
            popped = temp_stack.pop()
            while temp_stack:
                self.stack.append(temp_stack.pop())
            return popped
        return None

    def peek(self) -> int:
        temp_stack = []
        if not self.empty():
            while self.stack:
                temp_stack.append(self.stack.pop())
            peeked = temp_stack[-1]
            while temp_stack:
                self.stack.append(temp_stack.pop())
            return peeked
        return None

    def empty(self) -> bool:
        return self.len == 0


obj = MyQueue()
obj.push(5)
obj.push(6)
print(obj.peek())
print(obj.pop())
print(obj.empty())