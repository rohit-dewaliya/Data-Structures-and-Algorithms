class MyStack:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.pop(0))

    def pop(self) -> int:
        if not self.empty():
            return self.queue.pop(0)
        return None

    def top(self) -> int:
        if not self.empty():
            return self.queue[0]
        return None

    def empty(self) -> bool:
        return len(self.queue) == 0


obj = MyStack()
obj.push(5)
obj.push(6)
print(obj.pop())    # 6
print(obj.top())    # 5
print(obj.empty())  # False
