class MinStack:
    def __init__(self):
        self.stack = []
        self.min = float('inf')

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
            self.min = val
        else:
            self.stack.append((val, min(val, self.min)))
            self.min = min(val, self.min)

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.min = self.stack[-1][1] if self.stack else float('inf')

    def top(self) -> int:
        return self.stack[-1][0] if self.stack else None

    def getMin(self) -> int:
        return self.stack[-1][1] if self.stack else None
